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
my_chat_id=env('TG_MY_CHATID')

bot=telebot.TeleBot(token)

logger=logging.getLogger(__name__)

@bot.message_handler(commands=["start"])
def start_func(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Услуги")
    button_2 = types.KeyboardButton(text="Портфолио")
    button_3 = types.KeyboardButton(text='О нас')
    button_4 = types.KeyboardButton(text='Контакты')
    button_5 =  types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button_1,button_2,button_3,button_4,button_5)
    bot.send_message(message.chat.id, "Приветствуем вас!\nМы IT-консалтинговая кампания Project Infinity, предоставлем услуги различного спектра в IT пространстве!",reply_markup=keyboard)



def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на наш сайт", url="https://project-infinity.kz")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Информация о нас',reply_markup=keyboard)


def send_request_from_django(obj):
    pass


def request_second_step(message,*args):
    bot.send_message(message.chat.id,'Контактный номер или ник в телеграмме')
    bot.register_next_step_handler(message,request_third_step,message.text)

def request_third_step(message,*args):
    logger.warning(args)
    bot.send_message(message.chat.id, 'Что вас заинтересовало, и что бы вы хотели узнать?')
    bot.register_next_step_handler(message,request_final_step,args[0],message.text)
    
def request_final_step(message,*args):
    logger.warning(f"ARGS:{args} {message.text}")
    bot.send_message(message.chat.id,'Спасибо за вашу заявку! С вами свяжутся в ближайшее время!')
    mes=f'Новая заявка! (БОТ)\nИмя: {args[0]}\nКонтакт: {args[1]}\nСодержание: {message.text}'
    bot.send_message(my_chat_id,mes)

    

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
        bot.send_message(message.chat.id,'Ваше имя')
        bot.register_next_step_handler(message,request_second_step)

if __name__=="__main__":
    bot.infinity_polling()