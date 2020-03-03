import requests

import os
from iss_api import get_lat_lng

def get_earthquake():

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')

    lat, lon = get_lat_lng()

    query = {'p': lat + ',' + lon, 'format': 'json', 'filter': 'all', 'client_id': user_id, 'client_secret': key}
    url = 'https://api.aerisapi.com/earthquakes/closest/'
    data = requests.get(url, params=query).json()

    return data

def return_quake():
    
    data = get_earthquake()

    if data['success']:
        if data['response']:
            magnitude = data['response'][0]['report']['mag']
            return magnitude
        else:
            return None