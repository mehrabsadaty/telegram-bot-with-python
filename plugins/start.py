from pyrogram import Client , filters
from pyrogram.types import Message



@Client.on_message(filters.text)
def my_handler (client : Client , massage : Message):
    massage.reply_text("hello")

