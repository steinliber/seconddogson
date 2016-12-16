# -*- coding: utf-8 -*-
from settings import WEATHER_ACCESS_TOKEN, LOCATION, LANGUAGE, UNIT, WEATHER_URL, SUGGEST_URL
import requests

# 天气emoji
# thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
# drizzle = u'\U0001F4A7'         # Code: 300's
# rain = u'\U00002614'            # Code: 500's
# snowflake = u'\U00002744'       # Code: 600's snowflake
# snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
# atmosphere = u'\U0001F301'      # Code: 700's foogy
# clearSky = u'\U00002600'        # Code: 800 clear sky
# fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
# clouds = u'\U00002601'          # Code: 802-803-804 clouds general
# hot = u'\U0001F525'             # Code: 904
# defaultEmoji = u'\U0001F300'
degree_sign= u'\N{DEGREE SIGN}'
weather_map = {
    '0': '\U00002600',
    '1': '\U00002600',
    '2': '\U00002600',
    '3': '\U00002600',
    '4': '\U00002601',
    '5': '\U00002601',
    '6': '\U00002601',
    '7': '\U00002601',
    '8': '\U00002601',
    '9': '\U000026C5',
    '10': '\U00002614',
    '11': '\U0001F4A8',
    '12': '\U0001F4A8',
    '13': '\U0001F4A7',
    '14': '\U00002614',
    '15': '\U00002614',
    '16': '\U0001F4A8',
    '17': '\U0001F4A8',
    '18': '\U0001F4A8',
    '19': '\U00002744',
    '20': '\U00002744',
    '21': '\U000026C4',
    '22': '\U000026C4',
    '23': '\U000026C4',
    '24': '\U000026C4',
    '25': '\U000026C4',
    '30': '\U0001F301',
    '31': '\U0001F301',
    '38': '\U0001F525'
}


class WeatherAPI():
    def __init__(self, location=LOCATION):
        self.location = location

    def get_weather(self, start=0, days=5):
        weather_text = self.location + ', ' + 'China: \n'
        params = {
            'key': WEATHER_ACCESS_TOKEN, 'location': self.location, 'language': LANGUAGE,
            'unit': UNIT, 'start': start, 'days': days}
        data = requests.get(WEATHER_URL, params=params)
        return_data = data.json()['results'][0]['daily']
        for weather in return_data:
            weather_len = len(weather['date'])
            weather_text += weather['date'] + ' -> ' + '白天: ' + weather['text_day'] + self._get_emoji(weather['code_day']) + '  晚上: ' + weather['text_night'] + self._get_emoji(weather['code_night']) + '\n'
            weather_text += ' ' * weather_len + '    ' + '最高温度: ' + weather['high'] + degree_sign + 'C  -  ' + '最低温度: ' + weather['low'] + degree_sign + 'C\n'
            weather_text += ' ' * weather_len + '    ' + '风力: ' + weather['wind_scale'] + '  风速: ' + weather['wind_speed'] + 'km/h\n'
        return weather_text

    def get_suggestion(self):
        params = {
            'key': WEATHER_ACCESS_TOKEN, 'location': self.location, 'language': LANGUAGE}
        data = requests.get(SUGGEST_URL, params=params)
        print(data.json()['results'][0]['suggestion'])

    def _get_emoji(self, weather_id):
        return weather_map.get(weather_id, u'\U0001F300')