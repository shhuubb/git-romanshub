import telebot
from telebot import types

bot = telebot.TeleBot('6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ')


# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a custom keyboard with buttons
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Найти объем сферы')
    button2 = types.KeyboardButton('Найти площадь поверхности сферы')
    button3 = types.KeyboardButton('Найти объем конуса')

    keyboard.add(button1, button2, button3)

    # Send a welcome message with the custom keyboard
    bot.reply_to(message, "Этот бот поможет тебе решить эти формулы:", reply_markup=keyboard)


# Handle button clicks
@bot.message_handler(func=lambda message: message.text == 'Button 1')
def handle_button1(message):
    # Perform action for Button 1
    bot.reply_to(message, "You pressed Button 1!")


@bot.message_handler(func=lambda message: message.text == 'Button 2')
def handle_button2(message):
    # Perform action for Button 2
    bot.reply_to(message, "You pressed Button 2!")


@bot.message_handler(func=lambda message: message.text == 'Button 3')
def handle_button3(message):
    # Perform action for Button 3
    bot.reply_to(message, "You pressed Button 3!")


# Handle user messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Respond to user message
    bot.reply_to(message, "You said: " + message.text)







# Start the bot
bot.polling()