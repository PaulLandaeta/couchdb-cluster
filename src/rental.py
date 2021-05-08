import requests
import json
from random import randrange, choice, random
import utils.constants as cons
from requests.models import HTTPBasicAuth
URL = 'http://127.0.0.1:5984/club_de_videos/'
USERNAME = 'admin'
PASSWORD = '123456'

def read_client():
    # TODO: read clients from couchDB
    clients = requests.get('http://127.0.0.1:5984/club_de_videos/_design/videos/_view/clients',auth=HTTPBasicAuth(USERNAME, PASSWORD))
    json_data = json.loads(clients.content)
    return json_data


def read_copies():
    # TODO: read clients from couchDB
    copies = requests.get('http://127.0.0.1:5984/club_de_videos/_design/videos/_view/copies',auth=HTTPBasicAuth(USERNAME, PASSWORD))
    json_data = json.loads(copies.content)
    return json_data


def store_retanls():
    clients = read_client()
    copies = read_copies()
    for copy in copies:
        for client in clients: 
            if (choice([0,1]) == 1):
                rental = {
                    "type": "rental",
                    "client": client,
                    "copy": copy,
                    "date_rental": "08/05/2021",
                    "nro_day": choice([1,2,3,4]),
                    "date_return":""
                }
                requests.post(URL, json=rental, auth=HTTPBasicAuth(USERNAME, PASSWORD))
                print('Retanls Loaded!!!')
