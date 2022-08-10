import telebot
from telebot import types

bot = telebot.TeleBot('5401086428:AAGHneNctvrk-XQ4xCTagnIp7OprTQsL6yQ')

#барои қабул кардани СМСои мизоҷ
@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "салом":
        bot.send_message(message.chat.id, f"Тдам салом {message.from_user.first_name}", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id: {message.from_user.id}", parse_mode="html")
    elif message.text == "чи":
        bot.send_message(message.chat.id, "Корт набоша", parse_mode="html")
    elif message.text == "?":
        bot.send_message(message.chat.id, "Биё сара вайрон наку", parse_mode="html")
    elif message.text == 'что':
        bot.send_message(message.chat.id, f"Аму гапо карочи", parse_mode="html")
    elif message.text == "эээ":
        bot.send_message(message.chat.id, "чи эээээ гуфтеси?", parse_mode="html")
    elif message.text == "ягон музика равон ку":
        music = open('ddd.mp3', "rb") 
        bot.send_voice(message.chat.id, f'ин гуш к музикара {music}', parse_mode="html" ) #ами командара дуруст кардан лозим
    elif message.text == "photo":
        photo = open('images.jfif', "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f"Абача тоҷикӣ гап зан нафаҳмидм", parse_mode="html")


#барои қабул кардани контентои мизоҷ
@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    markup = types.InlineKeyboardMarkup
    bot.send_message(message.chat.id, "И сурата ай куҷо ёфтӣ?")
#
# #барои созтани кнопкаҳо
#
# @bot.message_handler(commands=["website"])
# def get_user_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Open website", url = 'google.com'))
#     bot.send_message(message.chat.id, "Go to the website", reply_markup=markup)

bot.polling(none_stop=True)

