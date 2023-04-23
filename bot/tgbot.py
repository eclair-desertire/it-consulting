from django.conf import settings
import logging
import telebot
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file='./.env')

token=env('TG_BOT_TOKEN')

bot=telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_func(message):
    bot.send_message(message.chat.id, "")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__=="__main__":
    bot.infinity_polling()