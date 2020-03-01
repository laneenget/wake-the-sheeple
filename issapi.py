import requests

def get_iss():

    data = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']
    return lat, lon