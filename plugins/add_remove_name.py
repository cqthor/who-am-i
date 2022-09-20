from pyrogram import Client, filters
from pyrogram.types import Message

from plugins import OWNER, db, titles


@Client.on_message(filters.command('create_table') & filters.user(OWNER))
async def create_table(_, message: Message):
    try:
        table = message.text.split(' ')[1]
    except:
        return await message.reply("Usage: /create_table <table>")
    db.create_table(table)
    titles.append(table)
    await message.reply_text(f"Table {table} created")


@Client.on_message(filters.command('del_table') & filters.user(OWNER))
async def del_table(_, message: Message):
    try:
        table = message.text.split(' ')[1]
    except:
        return await message.reply("Usage: /del_table <table>")
    db.del_table(table)
    titles.remove(table)
    await message.reply_text(f"Table {table} deleted")


@Client.on_message(filters.command('edit_table') & filters.user(OWNER))
async def edit_table(_, message: Message):
    try:
        table = message.text.split(' ')[1]
        new_table = message.text.split(' ')[2]
    except:
        return await message.reply("Usage: /edit_table <table> <new_table>")
    db.edit_table(table, new_table)
    titles.remove(table)
    titles.append(new_table)
    await message.reply_text(f"Table {table} edited to {new_table}")


@Client.on_message(filters.command('add_name') & filters.user(OWNER))
async def add_name(_, message: Message):
    try:
        table = message.text.split(' ')[1]
        name = message.text.replace("/add_name ", "")
        name = name.replace(table, "")
        name = name.strip()
    except:
        return await message.reply("Usage: /add_name <table> <name>")
    db.add_name(table, name)
    await message.reply_text(f"Name {name} added to {table}")


@Client.on_message(filters.command('del_name') & filters.user(OWNER))
async def del_name(_, message: Message):
    try:
        table = message.text.split(' ')[1]
        name = message.text.replace("/del_name ", "")
        name = name.replace(table, "")
        name = name.strip()
    except:
        return await message.reply("Usage: /del_name <table> <name>")
    db.del_name(table, name)
    await message.reply_text(f"Name {name} deleted from {table}")
