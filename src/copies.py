import json
import requests
import utils.constants as cons
from requests.models import HTTPBasicAuth


def read_movies():
    with open('data/movies.json') as f:
        movies = json.load(f)
    return movies


def store_movies():
    movies = read_movies()
    for movie in movies:
        copy = {
            type: "copy",
            date_state: "2021-10-22",
            state: "prestamp",
            movie: movie
        }
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
    print('Copies Loaded!!!')
