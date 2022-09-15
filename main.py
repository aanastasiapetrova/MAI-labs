from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)  # Создаем новое приложение


# Загрузка данных из файла
def load_chat():
    with open('chat.json', 'r') as json_file:
        data = json.load(json_file)  # Зарузить файл в переменную data
        return data['messages']


all_messages = load_chat()  # Список всех сообщений


# Запись данных в файл
def save_chat():
    data = {'messages': all_messages}
    with open('chat.json', 'w') as json_file:
        json.dump(data, json_file)


@app.route('/chat')
def display_chat():
    return render_template('form.html')


@app.route('/')
def index_page():
    return "Welcome to my Messenger"


@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}


# Функция, которая добавляет новые сообщения
def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S %d.%m.%Y"),
    }
    all_messages.append(new_message)


# Функция для отправки сообщения
@app.route('/send_message')
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    save_chat()
    return 'Ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Запуск приложения
