from main import StreamBot
from pyrogram import filters

@StreamBot.on_message(filters.command('start'))
async def start(bot,msg):
    await msg.reply('hello')