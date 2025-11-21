from pyrogram import Client , filters
from pyrogram.types import Message , ReplyKeyboardMarkup



@Client.on_message(filters.command("start"))
def my_handler (client : Client , massage : Message):
    massage.reply_text("hello" ,
                       reply_markup=ReplyKeyboardMarkup(
                           [
                               ['/start' , 'hello'],
                               ['help']
                           ]
                       ,resize_keyboard= True) 
                       )
    

