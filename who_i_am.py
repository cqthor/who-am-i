from pyrogram import Client, enums

try:
    from config import API_HASH, API_ID, BOT_TOKEN
except:
    print("Please rename config_sample.py to config.py and fill in the required values.")
    exit(1)

plugins = dict(root="plugins")
bot = Client('bot', api_id=API_ID, api_hash=API_HASH,
             bot_token=BOT_TOKEN, plugins=plugins)

bot.parse_mode = enums.ParseMode.MARKDOWN
bot.run()
