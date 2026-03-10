# University Course Explorer

University Course Explorer is a Django-based web application that allows students to search and explore university courses using AI-powered embeddings and semantic search.

## Features
- Course search and exploration
- Semantic search using embeddings
- AI fine-tuning pipeline
- Integration with vector database (Weaviate)
- Django-based web interface

## Project Structure

manage.py – Django management file  
uni_course_exp/ – Django project settings  
uni_app/ – main application logic  
templates/ – HTML templates  
static/ – CSS and frontend files  

Additional scripts:

- `train_model.py` – model training
- `fine_tune.py` – fine-tuning pipeline
- `load_data_to_weaviate.py` – data ingestion
- `debug_embeddings.py` – embedding debugging
- `test_openapi.py` – API testing

## Database

The project uses `courses.sqlite` which contains the course dataset used for search and semantic analysis.

## Running the Project

###
Install dependencies

```bash
pip install -r requirements.txt
```

###
Run the Django server

```bash
python manage.py runserver
```

### 
Open in browser

http://127.0.0.1:8000

