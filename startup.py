class AtwFilt(object):

    DEFAULT_MSG = """hy {mention}..
    
Iam [{bot_name}](t.me/{bot_username}) 𝙾𝚛 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚌𝚊𝚕𝚕 𝚖𝚎 𝚊𝚜 [𝐅𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 𝐯𝟐](t.me/{bot_username}) 

𝙷𝚎𝚛𝚎  𝚈𝚘𝚞 𝙲𝚊𝚗 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝙼𝚘𝚟𝚒𝚎'𝚜, 𝙹𝚞𝚜𝚝 𝚂𝚎𝚗𝚝 [𝙼𝚘𝚟𝚒𝚎 𝙽𝚊𝚖𝚎](t.me/{bot_username})
𝚆𝚒𝚝𝚑 𝙿𝚛𝚘𝚙𝚎𝚛 #𝙶𝚘𝚘𝚐𝚕𝚎 𝚂𝚙𝚎𝚕𝚕𝚒𝚗𝚐..!!

𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 𝐂𝐥𝐢𝐜𝐤 /help"""

    HELP_MSG = """**
𝐇𝐲 👋  {mention}\n
𝐈 𝐂𝐚𝐧 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬\n 𝐉𝐮𝐬𝐭 𝐓𝐲𝐩𝐞i g 𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞\n
𝐀𝐧𝐝 𝐒𝐞𝐞 𝐓𝐡𝐚 𝐌𝐚𝐠𝐢𝐜 ✨"""
    DISCLAIMER = """
⚠️𝘿𝙄𝙎𝘾𝙇𝘼𝙄𝙈𝙀𝙍📍
𝙰𝚕𝚕 𝚝𝚑𝚎 𝚌𝚘𝚗𝚝𝚎𝚗𝚝𝚜 𝚑𝚎𝚛𝚎 𝚊𝚛𝚎 𝚎𝚒𝚝𝚑𝚎𝚛 𝚏𝚘𝚛𝚠𝚊𝚛𝚍𝚎𝚍 𝚏𝚛𝚘𝚖 𝚘𝚝𝚑𝚎𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚘𝚛 𝚌𝚘𝚙𝚒𝚎𝚍 𝚏𝚛𝚘𝚖 𝚝𝚑𝚎𝚖. 𝚆𝚎 𝚍𝚘𝚗'𝚝 𝚘𝚠𝚗 𝚊𝚗𝚢 𝚘𝚏 𝚝𝚑𝚎 𝙼𝚘𝚟𝚒𝚎𝚜 𝚘𝚛 𝚂𝚎𝚛𝚒𝚎𝚜.
𝙸𝚏 𝚈𝚘𝚞 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚛𝚒𝚐𝚑𝚝𝚜 𝚘𝚠𝚗𝚎𝚛 𝚊𝚗𝚍 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚛𝚎𝚖𝚘𝚟𝚎 𝚊𝚗𝚢 𝚌𝚎𝚛𝚝𝚊𝚒𝚗 𝚏𝚒𝚕𝚎𝚜, 𝙿𝚕𝚎𝚊𝚜𝚎 𝚛𝚎𝚙𝚘𝚛𝚝 𝚞𝚜, 𝚠𝚎 𝚊𝚛𝚎 𝚛𝚎𝚊𝚍𝚢 𝚝𝚘 𝚛𝚎𝚖𝚘𝚟𝚎 𝚝𝚑𝚘𝚜𝚎 𝚌𝚘𝚗𝚝𝚎𝚗𝚝 𝚊𝚜 𝚜𝚘𝚘𝚗 𝚊𝚜 𝚠𝚎 𝚌𝚊𝚗!
𝙰𝚍𝚖𝚒𝚗 𝙸𝚜 𝙽𝚘𝚝 𝚁𝚎𝚜𝚙𝚘𝚗𝚜𝚒𝚋𝚕𝚎 𝙵𝚘𝚛 𝚊𝚗𝚢 𝙳𝚒𝚛𝚎𝚌𝚝 & 𝚒𝚗𝚍𝚒𝚛𝚎𝚌𝚝 𝙿𝚛𝚘𝚏𝚒𝚝 𝚕𝚘𝚜𝚜
   **𝐀𝐃𝐌𝐈𝐍**
[𝐌𝐑.𝕍](t.me/RecallMvbadmin_Bot)
**𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫**
[𝐈𝐥𝐥𝐮𝐳𝐗](t.me/Grayhathacker767)"""

    ABOUT_MSG = """
---------🔴𝐀𝐁𝐎𝐔𝐓 𝐌𝐄🟢--------------
|
|○👨‍💻𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : [𝐈𝐥𝐥𝐮𝐳𝕏](t.me/mvbbotz)
|
|○📚𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : [𝐏𝐲𝐭𝐡𝐨𝐧 𝟑.𝟗.𝟏𝟎](https://www.python.org/)
|
|○🔧𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤 : [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝟏.𝟒.𝟏𝟐](https://docs.pyrogram.org/)
|
|○⚠️𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : [𝐔𝐳𝕏_𝐁𝐨𝐭𝐬](https://t.me/UZX_BOTS)     
|
|○⭐ 𝐃𝐚𝐭𝐚𝐁𝐚𝐬𝐞:[𝐌𝐎𝐍𝐆𝐎𝔻𝔹](https://mongodb.com)
|
|○💡𝐒𝐨𝐮𝐫𝐜𝐞𝐂𝐨𝐝𝐞: [𝐋𝐢𝐧𝐤](https://www.github.com/illuzX/AtwFilt)
|____


"""
#https://github.com/illuzX/AtwFilt/commit/42d151f309bcfc8fe667a9379a7609633705c4e

#FILE : <code>{file_name}</code> 
#❤️Size : <i>{file_size}</i>
#✅CAPTION: {file_caption}
    FILE_CAPTIONS = """ 
<code>💬 {title}</code> 
Size : <b>⌛ {size}</b>
━━━━━━━━━━━━━━━━━━━━━━
<b>[Mᴏᴠɪᴇ Bᴀᴢᴢᴇʀ](https://t.me/mvbzzer)</b
>\n[Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ Gʀᴏᴜᴘ](https://t.me/mvb_tg)
**"""

    
#~~Not work anymore~

    ADD_YOUR_GROUP = """**
𝐼 𝐶𝑎𝑛'𝑡 𝐹𝑖𝑛𝑑  <i>#{query}</i> 𝑖𝑛 𝑚𝑦 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒 𝑠𝑜 𝑝𝑙𝑒𝑎𝑠𝑒 𝑐ℎ𝑒𝑐𝑘 𝑦𝑜𝑢'𝑟𝑒 𝑒𝑛𝑡𝑒𝑟𝑒𝑑 𝑠𝑝𝑒𝑙𝑙𝑖𝑛𝑔 𝑖𝑛 #𝐺𝑜𝑜𝑔𝑙𝑒/ 𝑂𝑟 𝑇ℎ𝑎𝑡 𝑀𝑜𝑣𝑖𝑒 𝑁𝑜𝑡 𝑅𝑒𝑙𝑒𝑎𝑠𝑒𝑑 /**"""
 
    SPELL_CHECK = """
Hello 👋〘 {mention} 〙,
Couldn't Find {query}?  Please Click Your Request Movie Name"""
    GET_MOVIE_1 = """
** 📁 Here is What I Found In My Database** **For Your Query : #{title}**"""

    GET_MOVIE_2 = """
📽️ Requested Movie : {query}

👤 Requested By : {mention}

Uploder :[MOVIE BAZZER](t.me/mvbzzer)

© **{chat}**"""
