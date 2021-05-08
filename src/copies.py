import json
import requests
import utils.constants as cons
from requests.models import HTTPBasicAuth


def read_movies():
    with open('data/movies.json') as f:
        movies = json.load(f)
    return movies


def store_copies():
    movies = read_movies()
    for movie in movies:
        #TODO: create random number of copies
        copy = {
            "type": "copy",
            "status": "available",
            "movie": movie
        }
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
        requests.post(cons.URL, json=copy, auth=HTTPBasicAuth(
            cons.USERNAME, cons.PASSWORD))
    print('Copies Loaded!!!')
