import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media

from config import ADMINS
logger = logging.getLogger(__name__)

@illuzX.on_message(Worker.command('myDb'))
async def total(b, m):
    if m.from_user.id not in ADMINS:
        await m.delete()
    msg = await m.reply("please wait...β³οΈ", 
 quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f"ππΎππ°π» π΅πΈπ»π΄π: {total}")
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
