import requests

import os
from iss_api import get_lat_lng

def get_aq():

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')

    lat,lon = get_lat_lng()

    query = {'p': lat + ',' + lon, 'format': 'json', 'client_id': user_id, 'client_secret': key}
    url = 'https://api.aerisapi.com/airquality/'
    data = requests.get(url, params=query).json()
    
    return data

def return_aq():

    data = get_aq()

    if data['success']:
        aq = data['response'][0]['periods'][0]['category']
        return aq
    else:
        return None