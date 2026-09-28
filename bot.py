import telebot

# تۆکنی بۆتەکەت
TOKEN = '8816454023:AAGz_lgC9wzzaNyLv9u9jjHylm2dW3vStHs'
bot = telebot.TeleBot(TOKEN)

# چات ئایدی تایبەتی خۆت (تەنها تۆ دەتوانیت بۆتەکە بەکاربهێنیت)
MY_CHAT_ID = 766076610 

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.chat.id
    
    # پشکنین دەکات ئایا نامەکە لەلایەن خۆتەوە نێردراوە یان کەسێکی تر
    if user_id != MY_CHAT_ID:
        bot.send_message(user_id, "❌ ببوورە، ئەم بۆتە تایبەتە و تۆ ڕێپێدراو نییت بەکاریهێنیت.")
        return

    # کارەکانی تایبەت بە خۆت
    if message.text == '/start':
        bot.reply_to(message, "بەخێر هاتیتەوە، بۆتەکەت بە سەرکەوتوویی لە خزمەتتدایە! 🚀")
    else:
        bot.reply_to(message, f"نامەکەت گەیشت: {message.text}")

print("Bot is running...")
bot.infinity_polling()
