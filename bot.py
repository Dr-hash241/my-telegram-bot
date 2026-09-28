import telebot

# تۆکنی بۆتەکەت
TOKEN = "8925412158:AAE7_h_Coep39YriJYN4_ohwzBgmIfAnhaU"

# چات ئایدییەکەی خۆت (ئارمان)
ADMIN_CHAT_ID = 7749997725

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # پشکنین: ئەگەر نێردەرەکە تۆ نەبوویت، فەرامۆشی بکە و هیچ مەکە
    if message.chat.id != ADMIN_CHAT_ID:
        return
    
    # ئەگەر نێردەرەکە تۆ بوویت (ئارمان)، ئەوا لێرەدا کۆدەکەی C++ یان کارەکانت جێبەجێ بکە
    # بۆتەکە لێرەدا هیچ وەڵامێکی بێزارکەر یان replyـەک بۆ خۆت نانێرێت، بەڵکو بێدەنگ دەبێت
    
    # نموونە: لێرە دەتوانیت فەرمانەکانی خۆت دابنێیت بێ ئەوەی مەسجت بۆ بگەڕێنێتەوە
    user_text = message.text
    
    # (کۆدە گرنگەکەی خۆت لێرە دادەنێیت...)

bot.infinity_polling()
