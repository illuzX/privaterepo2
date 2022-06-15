import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media
import shutil
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
        disk_usage = psutil.disk_usage('/').percent
        await msg.edit(f"""                 ★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂{total}
          ★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴{used}({disk_usage}%)""")
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
