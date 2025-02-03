import logging
import logging.handlers
import os
import requests
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN_TELEGA')

ENDPOINT = 'localhost/api/check-imei/'
ENDPOINT_2 = 'localhost/api/white-list/'

bot = TeleBot(token=TELEGRAM_TOKEN)


data_dict = {}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='program.log',
    level=logging.DEBUG,
)


def check_whitelist(token, tg_id):
    try:
        whitelist = requests.post(
            ENDPOINT_2,
            headers=token,
            data={'tg_id': tg_id}
        )
        return whitelist
    except Exception:
        logging.error('сбой при проверке доступа')


def check_imei(imei, token):
    try:
        data = requests.post(
            ENDPOINT,
            headers=token,
            data={'imei': imei}
        )
        return data.json()
    except Exception:
        logging.error('сбой при проверки имея')


@bot.message_handler(content_types=['text'])
def check_list(massage):
    tg_id = massage.from_user.id
    if isinstance(check_whitelist(massage.text, tg_id), bool):
        if check_whitelist(massage.text, tg_id):
            data_dict[tg_id]=massage.text
            try:
                bot.send_message(
                    chat_id=massage.chat.id,
                    text='Введите ваш имей',
                )
            except Exception:
                logging.error('сбой при отправке сообщения')
        else:
            try:
                bot.send_message(
                    chat_id=massage.chat.id,
                    text='У вас нет доступа',
                )
            except Exception:
                logging.error('сбой при отправке сообщения')
    else:
        try:
            data = check_imei(massage.text, data_dict[tg_id])
            bot.send_message(
                    chat_id=massage.chat.id,
                    text=f'{data}',
                )
        except Exception:
            logging.error('сбой при отправке сообщения')
        


@bot.message_handler(commands=['start'])
def start(massage):
    chat = massage.chat
    try:
        logging.info('Начало отправки сообщения')
        bot.send_message(
            chat_id=chat.id,
            text='Добро пожаловать, введите свой секретный ключ',
        )
    except Exception:
        logging.error('сбой при отправке сообщения')


def main():
    bot.polling()


if __name__ == '__main__':
    main()
