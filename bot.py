import telebot

API_TOKEN = '7437070544:AAFCFregQklGuuSoy1KzFAY0XGegPYlBx90'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Telegram botman. Sizga qanday yordam bera olaman?\n\nBuyruqlar:\n/start - Botni ishga tushirish\n/help - Yordam\n/sticker - Stiker jo'natish")

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    # Bu yerda olingan to'g'ri stiker ID ni qo'shing
    sticker_id = 'CAACAgIAAxkBAAMSZrMrPyPPd9zWyRGySYd-Os5TyIUAAuhRAAKMaZlJw8QqezKEHv01BA'
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling()
