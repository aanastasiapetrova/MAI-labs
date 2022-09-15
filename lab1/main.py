import datetime
from config import open_weather_token, bot_token
import requests

def get_weather(city, open_weather_token):
    pass


def main():
    city = input('введите город ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
