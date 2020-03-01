import requests
from datetime import datetime

from pprint import pprint

def getData():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url).json()
    lat, lng = storeData(data)
    return lat, lng

def storeData(data):
    issData = {}
    latLngList = []
    timestamp =  data['timestamp']
    time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    lat = data['iss_position']['latitude']
    lng = data['iss_position']['longitude']
    
    return lat, lng