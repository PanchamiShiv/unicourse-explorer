from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
import numpy as np
from uni_app.models import  MergeCourse, CourseEra2, CourseCatalog, Coursera


class Command(BaseCommand):
    help = "Generate and store embeddings for courses"

    def handle(self, *args, **kwargs):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Generate embeddings for MergeCourse model
        courses = MergeCourse.objects.all()
        for course in courses:
            text = course.title  # Or use any other field you prefer
            embedding = model.encode(text)
            embedding_bytes = np.array(embedding).tobytes()
            course.embedding = embedding_bytes
            course.save()

        # Similarly for CourseEra2 model
        courses_era2 = CourseEra2.objects.all()
        for course in courses_era2:
            text = course.Course_name  # Or any other field
            embedding = model.encode(text)
            embedding_bytes = np.array(embedding).tobytes()
            course.embedding = embedding_bytes
            course.save()

        Course_Catalog  = CourseCatalog.objects.all()
        for course in Course_Catalog:
            text = course.Name  # Or any other field
            embedding = model.encode(text)
            embedding_bytes = np.array(embedding).tobytes()
            course.embedding = embedding_bytes
            course.save()

        Coursera_1 = Coursera.objects.all()
        for course in Coursera_1:
            text = course.title   # Or any other field
            embedding = model.encode(text)
            embedding_bytes = np.array(embedding).tobytes()
            course.embedding = embedding_bytes
            course.save()

        # And for CoursesData model
        # courses_data = CoursesData.objects.all()
        # for course in courses_data:
        #     text = course.CourseTitle  # Or any other field
        #     embedding = model.encode(text)
        #     embedding_bytes = np.array(embedding).tobytes()
        #     course.embedding = embedding_bytes
        #     course.save()
        #
        # edx = EdX.objects.all()
        # for course in edx:
        #     text = course.Name  # Or any other field
        #     embedding = model.encode(text)
        #     embedding_bytes = np.array(embedding).tobytes()
        #     course.embedding = embedding_bytes
        #     course.save()
        #
        # UdemyCourses = Udemy_Courses.objects.all()
        # for course in UdemyCourses:
        #     text = course.course_title  # Or any other field
        #     embedding = model.encode(text)
        #     embedding_bytes = np.array(embedding).tobytes()
        #     course.embedding = embedding_bytes
        #     course.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated and stored embeddings for all courses'))
