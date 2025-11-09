from pyrogram import Client

app = Client(
    "testBot",
    api_id=38646387,
    api_hash="b97141c7ab320d6922b4ef0e43211a33",
    bot_token="8294746458:AAEcfaA43EusMXtsO55156YG6E1pIF2nork",
    plugins=dict(root="plugins")
)

app.run()
