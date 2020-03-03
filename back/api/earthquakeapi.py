import requests

import os

def get_earthquake(lat, lon):

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')
    query = {'p': lat + ',' + lon, 'format': 'json', 'filter': 'all', 'client_id': user_id, 'client_secret': key}
    url = 'https://api.aerisapi.com/earthquakes/closest/'
    data = requests.get(url, params=query).json()
    if data['success']:
        if data['response']:
            magnitude = data['response'][0]['report']['mag']
            return magnitude
        else:
            return None