import telebot
from telebot import types
import requests
TOKEN = '5846126207:AAF_PMLzXPklIEYFYDjzc72IYhP7Km6RTC8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Инофрмация')
    item2 = types.KeyboardButton('Валюты')
    murkup.add(item1, item2)
    bot.send_message(message.chat.id, f'Добро пожаловать {message.from_user.first_name}' .format(message.from_user), reply_markup=murkup)
    bot.delete_message(message.chat.id, message.id)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'Privet':
        if message.text == 'Кнопка1':
            bot.send_message(message.chat.id, '123')
    elif message.text == 'Валюты':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('RUB')
        item2 = types.KeyboardButton('THB')
        back = types.KeyboardButton('<-Back')
        murkup.add(item1, item2, back)
        bot.send_message(message.chat.id, 'Выбери валюту :'.format(message.from_user), reply_markup=murkup)
        bot.delete_message(message.chat.id, message.id)
    elif message.text == 'RUB':
        bot.send_message(message.chat.id,'Kупить USDT за RUB: ' + get_binance_rates_rub())
        bot.delete_message(message.chat.id, message.id)
    elif message.text == 'THB':
        bot.send_message(message.chat.id, 'Kупить THB за USDT: ' + get_binance_rates_thb())
        bot.delete_message(message.chat.id, message.id)
    elif message.text == '<-Back':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Инофрмация')
        item2 = types.KeyboardButton('Валюты')
        murkup.add(item1, item2)
        bot.send_message(message.chat.id, 'Назад', reply_markup=murkup)
        bot.delete_message(message.chat.id, message.id)

def get_binance_rates_rub():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    headers = {
        'accept': '*/*',
        'User_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    params = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "asset": "USDT",
            "fiat": "RUB",
            "tradeType": "BUY"
        }
    response = requests.post(url=url, headers=headers, json=params).json()
    return response['data'][0]['adv']['price']
print(get_binance_rates_rub())

def get_binance_rates_thb():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    headers = {
        'accept': '*/*',
        'User_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    params = {
              "proMerchantAds": False,
              "page": 1,
              "rows": 10,
              "payTypes": [],
              "countries": [],
              "publisherType": None,
              "asset": "USDT",
              "fiat": "THB",
              "tradeType": "BUY"
            }
    response = requests.post(url=url, headers=headers, json=params).json()
    return response['data'][0]['adv']['price']
print(get_binance_rates_thb())


a = get_binance_rates_rub
b = get_binance_rates_thb


bot.polling(none_stop = True)