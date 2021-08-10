import os
import sys

from pyrogram import filters, Client
from pyrogram.types import Message

from config import SUDO_USERS

@Client.on_message(filters.command("restart") & filters.user(SUDO_USERS))
async def restart(c: Client, m: Message):
    await m.reply_text("Rebooting Omen......")
    args = [sys.executable, "-m", "main.py"]
    os.execl(sys.executable, *args)
