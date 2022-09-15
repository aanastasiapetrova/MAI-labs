from config import open_weather_token, bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import datetime

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне название города и я пришлю тебе погодную сводку! Формат ввода данных: Moscow.')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
        data = r.json()
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunrise']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f'Погода в городе: {city}\nТемпература: {cur_weather}°C\n'
                            f'Влажность: {humidity}%\nдавление: {pressure} мм.рт.ст\nВетер: {wind}м/с\n'
                            f'Восход солнца: {sunrise_timestamp}\n'
                            f'Хорошего дня!')
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    executor.start_polling(dp)
