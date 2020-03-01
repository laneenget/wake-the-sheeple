import requests
import os
import issapi

def get_aq(lat, lon):

    key = os.environ.get('WEATHER_KEY')
    user_id = os.environ.get('AERIS_USER')
    lat, lon = issapi.get_iss()
    data = requests.get(f'https://api.aerisapi.com/airquality/{lat, lon}?&format=json&fields=loc&client_id=D8cUXU9JP0KKpZzvNLcZM&client_secret=OPms7ZI8eXEmNCK0U0keQJNSmw4nxlsoMOkP')
    aq = data['response']['periods']['category']
    return aq