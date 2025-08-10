import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")
API_URL = os.getenv("OMDB_API_URL")


class MovieSearch:

    def __init__(self):
        print(API_KEY)
        print(API_URL)

    def get_movie_data(self, movie_name):
        params = {
            "apikey": API_KEY,
            "t": movie_name,
        }

        response = requests.get(url=API_URL, params=params)
        response.raise_for_status()
        return response.json()
