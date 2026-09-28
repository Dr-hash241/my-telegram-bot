import telebot

# تۆکنی بۆتەکەت
TOKEN = "8925412158:AAE7_h_Coep39YriJYN4_ohwzBgmIfAnhaU"

# چات ئایدییەکەی خۆت (ئارمان)
ADMIN_CHAT_ID = "7749997725"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # پشکنین بۆ ئەوەی بزانین ئایا خۆتی یان کەسێکی ترە
    if str(message.chat.id) == ADMIN_CHAT_ID:
        bot.reply_to(message, "سڵاو ئارمان گیان! بۆتەکە بە سەرکەوتوویی کار دەکات و تۆ بەڕێوەبەری.")
    else:
        bot.reply_to(message, "سڵاو! بۆتەکە خەریکە کار دەکات.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"پەیامەکەت وەرگیرا. چات ئایدییت: {message.chat.id}")

bot.infinity_polling()
