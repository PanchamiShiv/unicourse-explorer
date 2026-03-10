import os
import openai
from autocorrect import Speller
from dotenv import load_dotenv
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer, InputExample
from django.conf import settings

# Load API key from Django settings
openai.api_key = settings.OPENAI_API_KEY

def load_fine_tuned_model():
    """Load the fine-tuned SentenceTransformer model."""
    try:
        model = SentenceTransformer("./fine_tuned_model")
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load fine-tuned model: {e}")



def preprocess_query(query):
    """Preprocess the query by removing stopwords and applying autocorrect."""
    query = query.lower()
    spell = Speller()
    query = spell(query)
    stop_words = set(stopwords.words('english'))
    query_words = query.split()
    filtered_query = " ".join([word for word in query_words if word not in stop_words])

    # Map extracted keywords to known course-related keywords
    keyword_mapping = {
        "ai": ["machine learning", "neural networks", "deep learning"],
        "data science": ["statistics", "big data", "data visualization"],
        "security": ["cybersecurity", "encryption", "hacking", "IT security"],
        "python": ["python", "web application"],
        "programming": ["python", "java", "C++", "C"],
    }

    # Add mapped keywords to the query
    for key, mapped_keywords in keyword_mapping.items():
        if key in filtered_query:
            filtered_query += " " + " ".join(mapped_keywords)

    return filtered_query

def generate_gpt4_response(prompt):
    """
    Generate a response using OpenAI's GPT-4 model.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant specializing in course recommendations. Always prioritize relevance to the user's query."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
            top_p=0.9,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating response from GPT-4: {e}")
        return "Unable to generate a response at the moment. Please try again later."