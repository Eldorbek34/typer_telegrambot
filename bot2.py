import telebot

API_TOKEN = '7437070544:AAFCFregQklGuuSoy1KzFAY0XGegPYlBx90'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print(message.sticker.file_id)

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling()
