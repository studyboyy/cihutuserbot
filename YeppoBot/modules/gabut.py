from time import sleep
from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, edit_or_reply


@yeppo_cmd(pattern="teemo(?: |$)(.*)")
async def _(teemo):
    yins = await edit_or_reply(teemo, "`𝙏𝙚𝙚𝙢𝙢𝙤𝙤 𝙈𝙪𝙡𝙪 𝙇𝙪 😏`")
    sleep(2)
    await yins.edit("`𝙅𝙖𝙙𝙞𝙖𝙣 𝙅𝙪𝙜𝙖 𝙆𝙖𝙜𝙖𝙠 😂`")
    sleep(1)
    await yins.edit("`𝙏𝙖𝙥𝙞 𝙆𝙖𝙡𝙤 𝙇𝙪 𝙅𝙖𝙙𝙞𝙖𝙣, 𝙐𝙟𝙪𝙣𝙜-𝙐𝙟𝙪𝙣𝙜𝙣𝙮𝙖 𝙅𝙪𝙜𝙖 𝙆𝙚𝙣𝙖 𝙂𝙝𝙤𝙨𝙩𝙞𝙣𝙜 🤣`")


@yeppo_cmd(pattern="give(?: |$)(.*)")
async def _(giveaway):
    yeppo = await edit_or_reply(giveaway, "`𝙎𝙮𝙖𝙧𝙖𝙩 𝙄𝙠𝙪𝙩 𝙂𝙞𝙥𝙚𝙚𝙬𝙚𝙮`")
    sleep(2)
    await yeppo.edit("`𝙂𝙘𝙖𝙨𝙩 𝙈𝙞𝙣𝙞𝙢𝙖𝙡 10 𝙂𝙧𝙪𝙥`")
    sleep(1)
    await yeppo.edit("`𝙉𝙖𝙞𝙠 𝙊𝙨, 𝘿𝙖𝙣 𝙎𝙨 𝘽𝙪𝙠𝙩𝙞 𝙂𝙘𝙖𝙨𝙩`")


@yeppo_cmd(pattern="uno(?: |$)(.*)")
async def _(uno):
    xd = await edit_or_reply(uno, "`𝙆𝙖𝙠𝙠𝙠 👉👈`")
    sleep(2)
    await xd.edit("`𝘽𝙚𝙬𝙖𝙣 𝙐𝙣𝙤 𝙮𝙪𝙠 🙈`")
    sleep(1)
    await xd.edit("`𝙔𝙖𝙣𝙜 𝙆𝙖𝙡𝙖𝙝 𝙋𝙞𝙣𝙙𝙖𝙝 𝘼𝙜𝙖𝙢𝙖 🙊`")


CMD_HELP.update(
    {
        "gabut2": f"**Plugin : **`gabut2`\
        \n\n  »  **Perintah :** `{cmd}teemo`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}give`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}uno`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
    "
    }
)
