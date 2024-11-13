from telebot import TeleBot
from telebot import types
from random import randint


TOKEN = "7818984501:AAE9zi54Kl9UtBYiEFZNbEg8sK3h5QQTQr4"
bot = TeleBot(TOKEN)

a = 0

kb = types.ReplyKeyboardMarkup()
btn = types.KeyboardButton("just a button lol")
kb.add(btn)

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    global a
    bot.send_message(msg.chat.id, "поиграть хочешь??", reply_markup=kb)
    a = randint(1,10)





@bot.message_handler(content_types=["text"])
def handle_one(msg: types.Message):
    global a
    gnd = msg.text

    if a == 0:
        bot.send_message(msg.chat.id, "ты не начал игру как так")
    elif gnd.isdigit():
        gnd = int(gnd)
        if gnd == a:
            bot.send_message(msg.chat.id, "ты отгадал")
            a = 0       
        elif gnd > a:
            bot.send_message(msg.chat.id, "число больше чем загаданное")
        elif gnd < a:
            bot.send_message(msg.chat.id, "число меньше чем надо")

print("сервер запущен")
bot.polling()