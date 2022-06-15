class AtwFilt(object):

    DEFAULT_MSG = """hy {mention}..
    
Iam [{bot_name}](t.me/{bot_username}) 𝙾𝚛 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚌𝚊𝚕𝚕 𝚖𝚎 𝚊𝚜 [𝐅𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 𝐯𝟐](t.me/{bot_username}) 

𝙷𝚎𝚛𝚎  𝚈𝚘𝚞 𝙲𝚊𝚗 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝙼𝚘𝚟𝚒𝚎'𝚜, 𝙹𝚞𝚜𝚝 𝚂𝚎𝚗𝚝 [𝙼𝚘𝚟𝚒𝚎 𝙽𝚊𝚖𝚎](t.me/{bot_username})
𝚆𝚒𝚝𝚑 𝙿𝚛𝚘𝚙𝚎𝚛 #𝙶𝚘𝚘𝚐𝚕𝚎 𝚂𝚙𝚎𝚕𝚕𝚒𝚗𝚐..!!

𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 𝐂𝐥𝐢𝐜𝐤 /help"""

    HELP_MSG = """**
𝐇𝐲 👋 {mention}
𝐌𝐲 𝐍𝐚𝐦𝐞[{bot_name}](t.me/{bot_username}) 𝐈𝐬  𝐈 𝐂𝐚𝐧 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 𝐉𝐮𝐬𝐭 𝐓𝐲𝐩𝐞 𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 
𝐀𝐧𝐝 𝐒𝐞𝐞 𝐓𝐡𝐚 𝐌𝐚𝐠𝐢𝐜 ✨"""
    SOURCE_CODE = """
**REPO**
[𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞](https://www.github.com/illuzX/AtwFilt)
**𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫**
[𝐈𝐥𝐥𝐮𝐳𝐗](t.me/Grayhathacker767)"""

    ABOUT_MSG = """
𝐀𝐁𝐎𝐔𝐓 𝐌𝐄✏️

©️𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : [𝐈𝐥𝐥𝐮𝐳𝕏](t.me/mvbbotz)\n
🧾𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : [𝐏𝐲𝐭𝐡𝐨𝐧 𝟑.𝟗.𝟏𝟎](https://www.python.org/)\n
⌛𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝟏.𝟒.𝟏𝟐](https://docs.pyrogram.org/)\n
⚠️𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : [𝐔𝐳𝕏_𝐁𝐨𝐭𝐬](https://t.me/UZX_BOTS)\n
⭐ 𝐃𝐚𝐭𝐚𝐁𝐚𝐬𝐞:[𝐌𝐎𝐍𝐆𝐎𝔻𝔹](https://mongodb.com)\n


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
