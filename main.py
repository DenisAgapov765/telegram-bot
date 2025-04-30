import telebot

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'
USER_ID = 123456789  # Замените на свой Telegram ID

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.id == USER_ID:
        bot.reply_to(message, "Привет! Я бот и получил твоё сообщение: " + message.text)
    else:
        bot.reply_to(message, "Извините, доступ запрещен.")

bot.polling()
