import telebot
import requests

API_KEY = "Your_API_KEY"
bot = telebot.TeleBot(API_KEY)


def get_exchange_rate(base_currency, target_currency):
    url = f" https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    time_last_update = data["time_last_update_utc"]
    response_time = time_last_update.split(", ")
    cleaned_time = ", ".join(response_time[1:]).replace("+0000", "")

    return exchange_rate, cleaned_time


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = telebot.types.KeyboardButton("EUR/RUB")
    btn2 = telebot.types.KeyboardButton("USD/RUB")
    btn3 = telebot.types.KeyboardButton("USD/BYN")
    btn4 = telebot.types.KeyboardButton("EUR/BYN")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Выберите обменный курс:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "EUR/RUB")
def eur_rub(message):
    exchange_rate, cleaned_time = get_exchange_rate("EUR", "RUB")
    bot.send_message(message.chat.id, f"1 🇪🇺 = {exchange_rate} 🇷🇺\nВремя обновления: {cleaned_time}")


@bot.message_handler(func=lambda message: message.text == "USD/RUB")
def usd_rub(message):
    exchange_rate, cleaned_time = get_exchange_rate("USD", "RUB")
    bot.send_message(message.chat.id, f"1 🇺🇸 = {exchange_rate} 🇷🇺\nВремя обновления: {cleaned_time}")


@bot.message_handler(func=lambda message: message.text == "USD/BYN")
def usd_rub(message):
    exchange_rate, cleaned_time = get_exchange_rate("USD", "BYN")
    bot.send_message(message.chat.id, f"1 🇺🇸 = {exchange_rate} 🇧🇾\nВремя обновления: {cleaned_time}")


@bot.message_handler(func=lambda message: message.text == "EUR/BYN")
def usd_rub(message):
    exchange_rate, cleaned_time = get_exchange_rate("EUR", "BYN")
    bot.send_message(message.chat.id, f"1 🇪🇺 = {exchange_rate} 🇧🇾\nВремя обновления: {cleaned_time}")


bot.polling()
