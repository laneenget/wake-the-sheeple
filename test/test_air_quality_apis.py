import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from back.api.air_quality_api import return_aq


class TestAirApi(TestCase):
    
    @patch('back.api.air_quality_api.get_aq')
    def test_aq_data_parsing(self, mock_aq):
        mock_quality = "Bad"
        example_api_response = {'success': True, 'error': None, 'response': [{'id': None, 'loc': {'lat': 50.55583, 'long': 81.85833}, 'place': {'name': "ūst'-talovka", 'state': None, 'country': 'kz'}, 'periods': [{'dateTimeISO': '2020-03-03T07:00:00+06:00', 'timestamp': 1583197200, 'aqi': 59, 'category': mock_quality, 'color': 'FFFF00', 'method': 'airnow', 'dominant': 'pm2.5', 'pollutants': [{'type': 'o3', 'name': 'ozone', 'valuePPB': 33, 'valueUGM3': 68, 'aqi': 30, 'category': 'good', 'color': '00E400'}, {'type': 'pm2.5', 'name': 'particle matter (<2.5µm)', 'valuePPB': None, 'valueUGM3': 16, 'aqi': 59, 'category': 'moderate', 'color': 'FFFF00'}, {'type': 'pm10', 'name': 'particle matter (<10µm)', 'valuePPB': None, 'valueUGM3': 29, 'aqi': 27, 'category': 'good', 'color': '00E400'}, {'type': 'co', 'name': 'carbon monoxide', 'valuePPB': 137, 'valueUGM3': 157, 'aqi': 2, 'category': 'good', 'color': '00E400'}, {'type': 'no2', 'name': 'nitrogen dioxide', 'valuePPB': 7, 'valueUGM3': 14, 'aqi': 6, 'category': 'good', 'color': '00E400'}, {'type': 'so2', 'name': 'sulfur dioxide', 'valuePPB': 19, 'valueUGM3': 51, 'aqi': 26, 'category': 'good', 'color': '00E400'}]}], 'profile': {'tz': 'Asia/Almaty', 'sources': [{'name': 'CAMS'}], 'stations': None}}]}
        mock_aq.side_effect = [example_api_response]
        quality = return_aq()
        self.assertEqual(mock_quality, quality)

    @patch('back.api.air_quality_api.get_aq')    
    def test_aq_location_not_found(self, mock_aq):
        bad_api_response = {"success": False,"error": {"code": "invalid_location","description": "The requested location was not found."},"response": []}
        mock_aq.side_effect = [bad_api_response]
        expected_value = -1
        quality = return_aq()
        self.assertEqual(expected_value, quality)

    @patch('back.api.air_quality_api.get_aq')
    def test_aq_invalid_credentials(self, mock_aq):
        bad_api_response = {'success': False, 'error': {'code': 'invalid_client', 'description': 'The client provided is invalid.'}, 'response': []}
        mock_aq.side_effect = [bad_api_response]
        expected_value = 0
        quality = return_aq()
        self.assertEqual(expected_value, quality)
