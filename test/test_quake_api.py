import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from back.api.earthquake_api import return_quake

@patch('back.api.earthquake_api.get_earthquake')
def test_eq_data_parsing(self, mock_eq):
    mock_magnitude = 1.2
    example_api_response = {'success': True, 'error': None, 'response': [{'loc': {'long': -66.7465, 'lat': 17.9801}, 'report': {'id': 'pr2020063000', 'timestamp': 1583198248, 'dateTimeISO': '2020-03-02T21:17:28-04:00', 'mag': mock_magnitude, 'type': 'minor', 'depthKM': 13, 'depthMI': 8.08, 'region': '3km WSW of Tallaboa, Puerto Rico', 'location': '3km WSW of Tallaboa, Puerto Rico'}, 'place': {'name': 'tallaboa', 'state': '', 'country': 'pr'}, 'profile': {'tz': 'America/Puerto_Rico'}, 'relativeTo': {'lat': 17.9801, 'long': -66.7465, 'bearing': 180, 'bearingENG': 'S', 'distanceKM': 0, 'distanceMI': 0}}]}
    mock_eq.side_effect = [example_api_response]
    mag = return_quake()
    self.assertEqual(mock_magnitude, mag)