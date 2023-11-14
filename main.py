import telebot
from math import *

# Создание экземпляра бота
bot = telebot.TeleBot('6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши формулу по которой нужна помощь!\nобъем сферы\nобъем конуса')

# Обработчик ответа на вопрос о возрасте
@bot.message_handler(func=lambda message: True)
def sphere(message):
    if message.text == 'объем сферы':
        bot.send_message(message.chat.id, 'Введи значение R')

@bot.message_handler(func=lambda message: True)
def V_sphere(message):
    if message.text.isdigit():
        R = int(message.text)
        Vsphere = 4 / 3 * pi * R ** 3
        bot.send_message(message.chat.id, f'Объем: {Vsphere}')
        # Вывод значения формулы
        bot.send_message(message.chat.id, f'Значение формулы: {Vsphere}')

# Запуск бота
bot.polling()