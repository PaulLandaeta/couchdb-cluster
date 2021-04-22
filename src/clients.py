import json
import requests
from requests.models import HTTPBasicAuth

URL = 'http://127.0.0.1:5984/club_de_videos/'
USERNAME = 'admin'
PASSWORD = '123456'


def read_clients():
    with open('data/clients.json') as f:
        clients = json.load(f)
    return clients


def store_clients():
    clients = read_clients()
    for client in clients:
        response = requests.post(
            URL, json=client, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        print(response.content)
