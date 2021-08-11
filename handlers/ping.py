import os
import sys
import time

from pyrogram import filters, Client
from pyrogram.types import Message

from config import SUDO_USERS

start_time = time.time()
end_time = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Client.on_message(filters.command("ping") & filters.user(SUDO_USERS))
async def ping(c: Client, m: Message):
    await c.send_message("Ping")
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))

    gg.edit_text(
        "PONG!!\n"
        "Time Taken: <code>{}</code>\n"
        "Service uptime: <code>{}</code>".format(telegram_ping, uptime),
        parse_mode=ParseMode.HTML,
    )
