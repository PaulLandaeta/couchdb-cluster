import json
import requests
from requests.models import HTTPBasicAuth
from utils.constants import URL
from utils.constants import USERNAME
from utils.constants import PASSWORD


def read_clients():
    with open('data/clients.json') as f:
        clients = json.load(f)
    return clients


def store_clients():
    clients = read_clients()
    for client in clients:
        # TODO: verify request errors
        requests.post(URL, json=client, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print('Clients loaded')
