"""
    earthquake_api.py
    This file handles the earthquake API
"""
import requests

import os
from back.api.iss_api import get_lat_lng


# Get data from earthquake API
def get_earthquake():

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')

    lat, lon = get_lat_lng()

    query = {'p': lat + ',' + lon, 'format': 'json', 'filter': 'all', 'client_id': user_id, 'client_secret': key}
    url = 'https://api.aerisapi.com/earthquakes/closest/'
    data = requests.get(url, params=query).json()

    return data


# Pull needed data from the earthquake API request
def return_quake():
    
    data = get_earthquake()

    # Informing users of errors or success but not no relevant data
    if data['success']:
        if data['response']:
            magnitude = data['response'][0]['report']['mag']
            return magnitude
        else:
            return None
    elif data['error']['code']=='invalid_client':
        return 0
    elif data['error']['code']=='invalid_location':
        return -1