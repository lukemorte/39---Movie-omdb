# movie search

import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("OMDB_API_KEY")
API_URL = os.getenv("OMDB_API_URL")

request_data = {
    "apikey": API_KEY,
    "i": "tt3460252"
}


response = requests.get(url=API_URL, params=request_data)


response.raise_for_status()
print(response.url)
print(response.text)
