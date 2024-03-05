from telebot import TeleBot
from telebot.types import Message

bot=TeleBot('6790795950:AAFdUtVPj4PVUJ3BXPdBMwq8moMDNvQBLM4')

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id=message.chat.id
    full_name=message.from_user.full_name
    bot.send_message(chat_id,f"assalomu alaykum {full_name}")

@bot.message_handler(commands=['help'])
def help(message: Message):
    chat_id=message.chat.id
    full_name=message.from_user.full_name
    bot.send_message(chat_id,f"Bu bot nma qiloladi: Bu bot botga yuborilgan malumotlarni guruhga va yuborgan odamning oziga yuboradi")


@bot.message_handler(content_types=['text','photo','video','animation','sticker'])
def reaction_to_message(message: Message):
    chat_id=message.chat.id
    bot.copy_message(-1001988060178,chat_id,message.message_id)
    bot.send_message(-1001988060178,f"Bu habar {message.from_user.full_name} dan")




bot.polling()