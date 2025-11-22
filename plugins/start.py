from pyrogram import Client , filters
from pyrogram.types import Message , ReplyKeyboardMarkup ,InlineKeyboardMarkup , InlineKeyboardButton , CallbackQuery , ReplyKeyboardRemove



@Client.on_message(filters.command("start"))
def my_handler (client : Client , massage : Message):
    massage.reply_text("hello" ,
                       reply_markup=ReplyKeyboardMarkup(
                           [
                               ['/start' , 'hello'],
                               ['/rmv']
                           ]
                       ,resize_keyboard= True , one_time_keyboard=True) 
                       )
    
@Client.on_message(filters.command("rmv"))
def remove_markup (client : Client , massage : Message):
    massage.reply_text("removed"
                      , reply_markup= ReplyKeyboardRemove()
                      )
