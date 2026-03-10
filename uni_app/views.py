from django.shortcuts import render
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .models import MergeCourse, CourseEra2, CourseCatalog, Coursera
import logging
from .utils import load_fine_tuned_model, generate_gpt4_response, preprocess_query

# Load the SentenceTransformer model
model = load_fine_tuned_model()
logger = logging.getLogger(__name__)

def generate_query_embedding(query):
    """Generate an embedding for the user query using the fine-tuned SentenceTransformer."""
    return model.encode(query)

def get_most_similar_courses(query_embedding, course_embeddings, min_similarity=0.2, max_results=3):
    """Retrieve most similar courses based on cosine similarity."""
    similarities = cosine_similarity([query_embedding], course_embeddings)[0]
    filtered_indices = [
        idx for idx, similarity in enumerate(similarities) if similarity > min_similarity
    ]
    sorted_indices = sorted(filtered_indices, key=lambda idx: similarities[idx], reverse=True)
    limited_indices = sorted_indices[:max_results]
    limited_similarities = [similarities[idx] for idx in limited_indices]
    return limited_indices, limited_similarities

def prepare_retrieved_courses_text(matched_courses):
    """
    Prepare the formatted text of matched courses for GPT-4, ensuring it is clear and structured.
    """
    if not matched_courses:
        return "No relevant courses were retrieved from the database."

    retrieved_text = "Here are the courses retrieved from the database:\n\n"
    for i, course_info in enumerate(matched_courses, 1):
        course = course_info['course']
        similarity = course_info['similarity']
        course_title = (
            getattr(course, 'title', None)
            or getattr(course, 'Course_name', None)
            or "Unknown Title"
        )

        retrieved_text += (
            f"{i}. Title: {course_title}\n"
        )

    return retrieved_text

def search_course(request):
    """
    Handles the search query, retrieves similar courses, and generates a GPT-4 response.
    """
    matched_courses = []  # Store matched courses
    query = request.GET.get('query', '').strip()  # User query
    generated_response = ""  # Placeholder for GPT-4 response

    if query:
        try:
            # Step 1: Preprocess query and generate embeddings
            preprocessed_query = preprocess_query(query)
            query_embedding = generate_query_embedding(preprocessed_query)

            # Step 2: Retrieve course embeddings
            course_embeddings = []
            course_ids = []
            for model_class in [MergeCourse, CourseEra2, CourseCatalog, Coursera]:
                for course in model_class.objects.all():
                    if course.embedding:
                        try:
                            embedding = np.frombuffer(course.embedding, dtype=np.float32)
                            if embedding.shape == (384,):  # Check valid embedding shape
                                course_embeddings.append(embedding)
                                course_ids.append((model_class, course.id))
                        except Exception as e:
                            logger.error(f"Error processing embedding for course ID {course.id}: {e}")

            # Step 3: Find most similar courses
            if course_embeddings:
                course_embeddings = np.array(course_embeddings)
                similar_course_indices, similarities = get_most_similar_courses(
                    query_embedding, course_embeddings
                )

                # Fetch matched courses
                for index in similar_course_indices:
                    model_class, course_id = course_ids[index]
                    try:
                        course = model_class.objects.get(id=course_id)
                        similarity = round(similarities[similar_course_indices.index(index)], 2)
                        matched_courses.append({"course": course, "similarity": similarity})
                    except model_class.DoesNotExist:
                        logger.error(f"Course with ID {course_id} not found.")

            # Step 4: Prepare retrieved courses text
            retrieved_courses_text = prepare_retrieved_courses_text(matched_courses)

            # Step 5: Generate GPT-4 Response
            if matched_courses:
                prompt = (
                    f"User Query: \"{query}\"\n\n"
                    f"{retrieved_courses_text}\n\n"
                    "Based on the above courses, recommend the top 3 courses with a brief explanation "
                    "of why they are suitable for the user's query. If necessary, suggest alternative learning paths."
                )
            else:
                # Fallback prompt if no relevant courses are found
                prompt = (
                    f"User Query: \"{query}\"\n\n"
                    "No relevant courses were found in the database. Suggest alternative learning resources, "
                    "pathways, or topics that align with the user's interest."
                )

            generated_response = generate_gpt4_response(prompt)

        except Exception as e:
            logger.error(f"Error processing search: {e}")
            generated_response = "An error occurred while processing your request. Please try again later."

    return render(request, "home.html", {
        "query": query,
        "matched_courses": matched_courses,
        "generated_response": generated_response,
    })

def userview(request):
    """Render the home page without any search."""
    return render(request, "home.html")