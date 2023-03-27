# (c) Blazelink
import asyncio
import os
from asyncio import TimeoutError
from urllib.parse import quote_plus

from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Blazelink.bot import StreamBot
from Blazelink.utils.database import Database
from Blazelink.utils.file_properties import get_name, get_hash, get_media_file_size
from Blazelink.utils.human_readable import humanbytes
from Blazelink.vars import Var

db = Database(Var.DATABASE_URL, Var.name)


@StreamBot.on_message((filters.private) & (filters.video | filters.audio | filters.document), group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ [Blazelink Goel](https://github.com/Santo-Philip) ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",

                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>𝙹𝙾𝙸𝙽 UPDATES CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),

            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ʙᴏss** [Blazelink](https://t.me/BlazingSquad)",

                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        await c.send_sticker(chat_id=Var.BIN_CHANNEL,sticker="CAACAgUAAxkBAALqi2QgAAH90AcInpSJ2SUtnjYETOB5kAACOgADqZrmFjr5YnFvFg0fLwQ")

        msg_text = """<i><u>𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>[📥 Dᴏᴡɴʟᴏᴀᴅ]({})  [🖥 WATCH]({}) </b>\n\n<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE</b>"""
        log_text = """<i><u>𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>📥 Dᴏᴡɴʟᴏᴀᴅ : {} </b> \n\n <b>🖥 WATCH : {} </b>"""
        await c.send_message(
            chat_id=Var.FILES_CHANNEL,
            text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n\n**" + log_text.format(
                get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            disable_web_page_preview=True,
        )
        await c.send_sticker(chat_id=Var.FILES_CHANNEL,sticker="CAACAgUAAxkBAALqj2QgAQIenNs-tgmAotZOzLd6b7qUAAJeAAOpmuYW-B1yGrfN828vBA")
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("STREAM 🖥", url=stream_link),
                                                InlineKeyboardButton('DOWNLOAD 📥', url=online_link)]])
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`",
                             disable_web_page_preview=True)\


@StreamBot.on_message((filters.group) & (filters.command("link")) & (filters.video | filters.audio | filters.document), group=4)
async def group_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ [Blazelink Goel](https://github.com/Santo-Philip) ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",

                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>𝙹𝙾𝙸𝙽 UPDATES CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),

            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ʙᴏss** [Blazelink](https://t.me/BlazingSquad)",

                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.FILES_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
#        await c.send_sticker(chat_id=Var.FILES_CHANNEL,sticker="CAACAgUAAxkBAALqi2QgAAH90AcInpSJ2SUtnjYETOB5kAACOgADqZrmFjr5YnFvFg0fLwQ")

        msg_text = """<i><u>𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>[📥 Dᴏᴡɴʟᴏᴀᴅ]({})  [🖥 WATCH]({}) </b>\n\n<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE</b>"""
        log_text = """<i><u>𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>📥 Dᴏᴡɴʟᴏᴀᴅ : {} </b> \n\n <b>🖥 WATCH : {} </b>"""
        await c.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n\n**" + log_text.format(
                get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            disable_web_page_preview=True,
        )
#        await c.send_sticker(chat_id=Var.BIN_CHANNEL,sticker="CAACAgUAAxkBAALqj2QgAQIenNs-tgmAotZOzLd6b7qUAAJeAAOpmuYW-B1yGrfN828vBA")
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("STREAM 🖥", url=stream_link),
                                                InlineKeyboardButton('DOWNLOAD 📥', url=online_link)]])
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`",
                             disable_web_page_preview=True)


@StreamBot.on_message((filters.channel) & (filters.video | filters.audio | filters.document), group=4)
async def channel_receive_handler(c: Client, m: Message):
    try:
        log_msg = await m.forward(chat_id=Var.FILES_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        log_text = """<i><u>🔗 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n<b>💬 Channel : </b>{}\n<b>💡 Channel ID :</b>{}\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>📥 Dᴏᴡɴʟᴏᴀᴅ : {} </b> \n\n <b>🖥 WATCH : {} </b>"""

#        await c.send_sticker(chat_id=Var.FILES_CHANNEL,sticker="CAACAgUAAxkBAALqi2QgAAH90AcInpSJ2SUtnjYETOB5kAACOgADqZrmFjr5YnFvFg0fLwQ")

        await c.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n\n**" + log_text.format(m.chat.title,m.chat.id,
                get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            disable_web_page_preview=True,
        )
#        await c.send_sticker(chat_id=Var.BIN_CHANNEL,sticker="CAACAgUAAxkBAALqj2QgAQIenNs-tgmAotZOzLd6b7qUAAJeAAOpmuYW-B1yGrfN828vBA")
        await c.edit_message_reply_markup(chat_id=m.chat.id, message_id=m.id, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("STREAM 🖥", url=stream_link),
              InlineKeyboardButton('DOWNLOAD 📥', url=online_link)]]))
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL,
                         text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`",
                         disable_web_page_preview=True)
    except Exception as w:
        await c.send_message(chat_id=m.chat.id, text=f"**#ERROR_TRACKEBACK:** `{w}`\n\n Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{w}**")



