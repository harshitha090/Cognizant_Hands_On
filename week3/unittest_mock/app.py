import requests
from database import get_user_from_db

def fetch_user(user_id):
    return get_user_from_db(user_id)

def fetch_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()