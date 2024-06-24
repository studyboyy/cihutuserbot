# imported from ppe-remix by @heyworld & @DeletedUser420
# Based Code by @adekmaulana
# Improve by @aidilaryanto


from secrets import choice

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, deEmojify, eod
from Stringyins import get_string


@yeppo_cmd(pattern="waifu(?: |$)(.*)")
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer(get_string("waifu_1"))
            return
    animus = [15, 30, 32, 33, 40, 41, 42, 48, 55, 58]
    sticcers = await animu.client.inline_query(
        "stickerizerbot", f"#{choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await eod(
            animu, get_string("waifu_2")
        )


CMD_HELP.update(
    {
        "waifu": f"**Plugin : **`waifu`\
        \n\n  »  **Perintah :** `{cmd}waifu <text>`\
        \n  »  **Kegunaan : **Untuk Mengcuston sticer anime dengan text yg di tentukan.\
    "
    }
)
