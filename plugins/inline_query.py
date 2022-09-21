from random import choice

from pyrogram import Client
from pyrogram.types import (InlineQuery, InlineQueryResultArticle,
                            InputTextMessageContent)

from plugins import db, titles


@Client.on_inline_query()
async def inline_query(_, inline_query: InlineQuery):
    user_id = inline_query.from_user.id
    query = inline_query.query.strip()
    results = []
    for title in titles:
        rename_title = title.replace("_", " ")
        if title.lower().startswith(query.lower()):
            try:
                name = db.get_users_name(user_id, title)[2]
            except:
                try:
                    name = choice(db.get_names(title))[0]
                except:
                    continue
                db.add_users_name(user_id, title, name)
            results.append(InlineQueryResultArticle(
                id=title,
                title=rename_title,
                description=f"Who are you in {rename_title}?",
                input_message_content=InputTextMessageContent(
                    f'You are {name} in {rename_title}')
            ))
    await inline_query.answer(
        results=results,
        cache_time=1
    )
