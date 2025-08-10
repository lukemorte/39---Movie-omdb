# movie search

import tkinter
from movie_search import MovieSearch
import pprint



movie_search = MovieSearch()

isLooped = True

while isLooped:
    movie_name = input("Enter the movie: ")
    data = movie_search.get_movie_data(movie_name)

    pprint.pprint(data)
