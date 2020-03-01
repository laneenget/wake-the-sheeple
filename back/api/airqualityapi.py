import requests
import os
import issapi

def get_aq(lat, lon):

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')
    lat, lon = issapi.getData()
    query = {'p': 'lat' + ',' + 'lon', 'format': 'json', 'client_id': user_id, 'client_secret': key}
    url = ('https://api.aerisapi.com/airquality/')
    data = requests.get(url, params=query).json()
    if data['success']:
        aq = data['response'][0]['periods'][0]['category']
        return aq
    else:
        return None