from django.conf import settings
from telebot import types
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
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Услуги")
    button_2 = types.KeyboardButton(text="Портфолио")
    button_3 = types.KeyboardButton(text='О нас')
    button_4 = types.KeyboardButton(text='Контакты')
    button_4 =  types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button_1,button_2,button_3,button_4)
    bot.send_message(message.chat.id, "Приветствуем вас!\nМы IT-консалтинговая фирма, предоставлем услуги различного спектра в IT пространстве!",reply_markup=keyboard)



def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на наш сайт", url="https://project-infinity.kz")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, str(message.chat.id),reply_markup=keyboard)

def send_request(text):
    bot.send_message(1392920598,text)
    

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if str(message.text).lower()=='услуги':
        bot.register_next_step_handler(message)
    if str(message.text).lower()=='портфолио':
        bot.register_next_step_handler(message)
    if str(message.text).lower()=='о нас':
        info_func(message)
    if str(message.text).lower()=='контакты':
        bot.register_next_step_handler(message)
    if str(message.text).lower()=='оставить заявку':
        bot.register_next_step_handler(message)

if __name__=="__main__":
    bot.infinity_polling()