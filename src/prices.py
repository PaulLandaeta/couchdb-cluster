import json
import requests
from requests.models import HTTPBasicAuth


URL = 'http://127.0.0.1:5984/club_de_videos/'
USERNAME = 'admin'
PASSWORD = '123456'


def store_prices():
    prices = {
        "type": "price",
        "one_day": 1,
        "two_days": 2,
        "three_days": 3,
        "four_days": 5,
        "five_days": 6
    }
    requests.post(URL, json=prices, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print('Prices Loaded!!!')
