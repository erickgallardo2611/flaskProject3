import datetime
import os
import time

import telebot

from connectionSQL import ConnectionDatabase


class BotTelegram():
    def __init__(self):
        self.API_TOKEN = None
        self.bot = None
        self.chat_id = None
        self.personas = 0


    def iniciar_bot(self):
        self.API_TOKEN = '5728395894:AAHtkIgVXXv8TAUfXodeQ9ppHQqEUBSSxwI'
        self.bot = telebot.TeleBot(self.API_TOKEN)


        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message, "Hola soy el bot, del banco..., nuestro id es: " + str(message.from_user.id))
            print("Hola soy el bot, del banco..., nuestro id es: "+str(message.from_user.id))
            self.chat_id = message.from_user.id
            while True:
                conn = ConnectionDatabase()
                conn.getConn()
                personas = conn.getLen()
                if(personas > 100):
                    self.bot.send_message(chat_id=self.chat_id,text="Alerta la tabla de registros esta por llenarse " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".")
                time.sleep(10)

        self.bot.polling()


