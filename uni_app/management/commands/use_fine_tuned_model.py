from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            model = SentenceTransformer("./fine_tuned_model")
            # Use the fine-tuned model for tasks here
            print("Fine-tuned model loaded successfully.")
        except Exception as e:
            print(f"Error loading fine-tuned model: {e}")
