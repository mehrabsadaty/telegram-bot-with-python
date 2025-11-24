from pyrogram import Client , filters
from pyrogram.types import Message , ReplyKeyboardMarkup ,InlineKeyboardMarkup , InlineKeyboardButton , CallbackQuery , ReplyKeyboardRemove 


@Client.on_message(filters.command("start"))
def my_handler (client : Client , massage : Message):
    massage.reply_text("hello" ,
                       reply_markup= InlineKeyboardMarkup(
                           [
                               [InlineKeyboardButton(text="button1" , callback_data="button1")] , [InlineKeyboardButton(text="button2" , callback_data="button2")] ,
                               [InlineKeyboardButton(text="button3" , url="https://google.com")],
                               [InlineKeyboardButton(text="click on" , callback_data="click")]
                           ]
                       ) 
                       )
    
@Client.on_message(filters.command("rmv"))
def remove_markup (client : Client , massage : Message):
    massage.reply_text("removed"
                      , reply_markup= ReplyKeyboardRemove()
                      )
