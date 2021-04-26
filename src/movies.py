import json
import requests
from requests.models import HTTPBasicAuth


URL = 'http://127.0.0.1:5984/club_de_videos/'
USERNAME = 'admin'
PASSWORD = '123456'


def read_movies():
    with open('data/movies.json') as f:
        movies = json.load(f)
    return movies


def store_movies():
    movies = read_movies()
    for movie in movies:
        movie.update({type: "movie"})
        requests.post(URL, json=movie, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print('Movies Loaded!!!')
