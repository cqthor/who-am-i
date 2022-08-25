from random import choice
from pyrogram.types import Message,  InlineQueryResultArticle, InputTextMessageContent, InlineQuery
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from db_helper import DBHelper
import config

db = DBHelper()

api_id = config.api_id
api_hash = config.api_hash
TOKEN = config.TOKEN

bot = Client('bot', api_id=api_id, api_hash=api_hash, bot_token=TOKEN)

owner = 841608283


@bot.on_inline_query()
async def inline_query(client, inline_query: InlineQuery):
    user_id = inline_query.from_user.id
    query = inline_query.query.strip()
    results = []
    titles = db.get_tables()
    for title in titles:
        rename_title = title.replace("_", " ")
        if title.lower().startswith(query.lower()):
            try:
                name = db.get_users_name(user_id, title)[2]
            except:
                name = choice(db.get_names(title))[0]
                db.add_users_name(user_id, title, name)
            results.append(InlineQueryResultArticle(
                id=title,
                title=rename_title,
                description=f"Who are you in {rename_title}?",
                input_message_content=InputTextMessageContent(
                    f'You are {name} in {rename_title}', parse_mode=ParseMode.MARKDOWN)
            ))
    await inline_query.answer(
        results=results,
        cache_time=1
    )


@bot.on_message(filters.command('create_table'))
async def create_table(client, message: Message):
    if message.from_user.id != owner:
        return
    try:
        table = message.text.split(' ')[1]
    except:
        return await message.reply("Usage: /create_table <table>", parse_mode=ParseMode.MARKDOWN)
    db.create_table(table)
    await message.reply_text(f"Table {table} created")


@bot.on_message(filters.command('del_table'))
async def del_table(client, message: Message):
    if message.from_user.id != owner:
        return
    try:
        table = message.text.split(' ')[1]
    except:
        return await message.reply("Usage: /del_table <table>", parse_mode=ParseMode.MARKDOWN)
    db.del_table(table)
    await message.reply_text(f"Table {table} deleted")


@bot.on_message(filters.command('edit_table'))
async def edit_table(client, message: Message):
    if message.from_user.id != owner:
        return
    try:
        table = message.text.split(' ')[1]
        new_table = message.text.split(' ')[2]
    except:
        return await message.reply("Usage: /edit_table <table> <new_table>", parse_mode=ParseMode.MARKDOWN)
    db.edit_table(table, new_table)
    await message.reply_text(f"Table {table} edited to {new_table}")


@bot.on_message(filters.command('add_name'))
async def add_name(client, message: Message):
    if message.from_user.id != owner:
        return
    try:
        table = message.text.split(' ')[1]
        name = message.text.replace("/add_name ", "")
        name = name.replace(table, "")
        name = name.strip()
    except:
        return await message.reply("Usage: /add_name <table> <name>", parse_mode=ParseMode.MARKDOWN)
    db.add_name(table, name)
    await message.reply_text(f"Name {name} added to {table}")


@bot.on_message(filters.command('del_name'))
async def del_name(client, message: Message):
    if message.from_user.id != owner:
        return
    try:
        table = message.text.split(' ')[1]
        name = message.text.replace("/del_name ", "")
        name = name.replace(table, "")
        name = name.strip()
    except:
        return await message.reply("Usage: /del_name <table> <name>", parse_mode=ParseMode.MARKDOWN)
    db.del_name(table, name)
    await message.reply_text(f"Name {name} deleted from {table}")


bot.run()
