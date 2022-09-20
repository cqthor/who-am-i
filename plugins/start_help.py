from pyrogram import Client, filters
from pyrogram.types import Message

from plugins import BOT_USERNAME, OWNER


@Client.on_message(filters.command('start') & filters.private)
async def start(_, message: Message):
    msg = f"""**Hello {message.from_user.mention}!**\nThis bot tell you who you are from chosen fictional universe.
Type `@{BOT_USERNAME}` <universe> in any chat to get a random name from a that universe"""
    await message.reply_text(msg)


@Client.on_message(filters.command('help'))
async def help(_, message: Message):
    if message.from_user.id == OWNER:
        text = f"""
**Commands:**

/create_table <table> - Create a table
/del_table <table> - Delete a table
/edit_table <table> <new_table> - Edit a table
/add_name <table> <name> - Add a name to a table
/del_name <table> <name> - Delete a name from a table
"""
    else:
        text = f"""
Type `@{BOT_USERNAME}` <universe> in any chat to get a random name from a that universe
"""
    await message.reply_text(text)
