import unittest
from unittest.mock import patch
from src.api.openweathermap import OpenWeatherMapAPI
from config.config import Config

class TestOpenWeatherMapAPI(unittest.TestCase):
    def setUp(self):
        self.api = OpenWeatherMapAPI()

    @patch('src.api.openweathermap.requests.get')
    def test_get_weather_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            'main': {'temp': 25},
            'weather': [{'main': 'Clear'}],
            'dt': 1622555400
        }

        result = self.api.get_weather_data('Delhi')

        self.assertEqual(result['main']['temp'], 25)
        self.assertEqual(result['weather'][0]['main'], 'Clear')

        mock_get.assert_called_once_with(
            Config.API_BASE_URL,
            params={
                'q': 'Delhi',
                'appid': Config.API_KEY,
                'units': 'metric'
            }
        )

if __name__ == '__main__':
    unittest.main()
