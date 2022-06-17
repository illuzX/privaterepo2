import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media
from plugins.database.users_chats_db import db
import shutil
import psutil
from config import ADMINS
logger = logging.getLogger(__name__)

@illuzX.on_message(Worker.command('stats'))
async def total(b, m):
    if m.from_user.id not in ADMINS:
        await m.delete()
    msg = await m.reply("please wait...⏳️", 
 quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f"""                 ★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂{total}"""
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
