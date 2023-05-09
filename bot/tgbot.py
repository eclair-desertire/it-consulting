from django.conf import settings
from telebot import types
import logging
import telebot
import environ
import requests
import time

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file='./.env')

token=env('TG_BOT_TOKEN')
my_chat_id=env('TG_MY_CHATID')
BOT_REQUEST_TOKEN=env('BOT_REQUEST_TOKEN')

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
    bot.send_message(message.chat.id, 'Мы являемся IT-консалтинговой компанией которая оказывает различные услуги в сфере IT. От аудита компании и обучения персонала до разработки высоконагруженных бизнес приложений.',reply_markup=keyboard)


def send_request_from_django(obj):
    name=obj.get('name')
    email=obj.get('email')
    phone=obj.get('phone')
    title=obj.get('title')
    description=obj.get('about')
    mes=f'Новая заявка с сайта!\nИмя:{name} , Почта: {email}\nТелефон:{phone}\nТема:{title}\nОписание:{description}'
    bot.send_message(my_chat_id,mes)


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

    
def services(message):
    r=requests.get('http://core:8000/api/services/',headers={'bot-request-token':BOT_REQUEST_TOKEN})
    logger.warning(r.text)
    data=r.json()
    logger.warning(data)
    for i in data['results']:
        image_url=str(i['image']).split('/')[-1]
        logger.warning(image_url)
        bot.send_photo(message.chat.id,photo=open('/app/media/'+image_url,'rb'))
        bot.send_message(message.chat.id,str(i['title'])+'\n'+str(i['description']))
        time.sleep(0.25)

def portfolio(message):
    r=requests.get('http://core:8000/api/portfolios/',headers={'bot-request-token':BOT_REQUEST_TOKEN})
    logger.warning(r.text)
    data=r.json()
    logger.warning(data)
    for i in data['results']:
        image_url=str(i['image']).split('/')[-1]
        logger.warning(image_url)
        bot.send_photo(message.chat.id,photo=open('/app/media/'+image_url,'rb'))
        bot.send_message(message.chat.id,str(i['title'])+'\n'+str(i['info']))
        time.sleep(0.25)

def contacts(message):
    r=requests.get('http://core:8000/api/contacts/',headers={'bot-request-token':BOT_REQUEST_TOKEN})
    logger.warning(r.text)
    data=r.json()
    logger.warning(data)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if str(message.text).lower()=='услуги':
        services(message)
    if str(message.text).lower()=='портфолио':
        portfolio(message)
    if str(message.text).lower()=='о нас':
        info_func(message)
    if str(message.text).lower()=='контакты':
        contacts(message)
    if str(message.text).lower()=='оставить заявку':
        bot.send_message(message.chat.id,'Ваше имя')
        bot.register_next_step_handler(message,request_second_step)

if __name__=="__main__":
    bot.infinity_polling()