from pyrogram import Client
from config import Config

app = Client(
    Config.TL_SESSION,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH
)

app.start()

print(app.get_me())
