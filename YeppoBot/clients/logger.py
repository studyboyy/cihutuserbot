# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from YeppoBot import BOT_VER as version
from YeppoBot import BOTLOG_CHATID
from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import bot, branch, tgbot
from YeppoBot.yeppo import yeppo_version as py_ver
from YeppoBot.yeppo import HOSTED_ON
# from YeppoBot.yeppo import checking


MSG_ON = """
❏ ʏᴇᴘᴘᴏ ᴜꜱᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼┅━━━━━╍━━━━━┅╾
├▹ ʏᴇᴘᴘᴏ ᴜꜱᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {} •[{}]•
├▹ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 Vᴇʀsɪᴏɴ - {}
├▹ Kᴇᴛɪᴋ .alive Uɴᴛᴜᴋ Mᴇɴɢᴇᴄᴇᴋ Bᴏᴛ
╰╼┅━━━━━╍━━━━━┅╾
"""


async def yeppo_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            yeppoUBOT = await tgbot.get_me()
            BOT_USERNAME = yeppoUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            yeppoUBOT = await tgbot.get_me()
            BOT_USERNAME = yeppoUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "ɪᴄʜɪʜᴏᴏᴅ ᴜꜱᴇʀʙᴏᴛ"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
