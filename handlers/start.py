from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from handlers.play import cb_admin_check
from config import BOT_USERNAME


@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hey {}!**\n\nI can play music In Voice Chats of Telegram Groups.I Have A lot of cool feature that will amaze You!\n\nHit /help to know more functions of mine.".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "🆘 Support", url=f"https://t.me/AnteikuUnion"), 
                    InlineKeyboardButton(
                        "Updates 🔉", url=f"https://t.me/SuzuyaUpdates"),
                ],
            ],
        ),
        reply_to_message_id=message.message_id,
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="Music Bot is still Awake!!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🆘 Support", url="https://t.me/AnteikuUnion"
                    ),
                ],
                [    
                    InlineKeyboardButton(
                        text="Search YT 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        text="Delete", callback_data="del"
                    ),
                ],
            ],
        ),
    )



@Client.on_message(filters.command(["help", "help@AnteikuMusicRobot"]) & filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        text="""**Anteiku Music : Help Menu**
╒════**「 Setup Guide 」**
├1.Promote bot as admin.
├ (with **Manage Voice Chats** rights)
├2.Turn on voice chat.
├3.Run `/play ``[song name]` in your chat.
├4.If userbot joins the chat, enjoy music.
├  If not, add @AnteikuMusicBot manually.
╘══════════════════
╒════**「 Music Player 」**
├ `/play` - Song Name : Plays Via Youtube.
├ `/dplay` - Song Name : Play Via Deezer.
├ `/splay` - Song Name : Play Via Jio Saavn.
├ `/playlist` - Shows playing song list.
├ `/current` - Shows now playing song .
├
╞══**「 Extras 」**
├ `/song` : Download song from YouTube.
├ `/vsong` : Download video from YouTube.
├ `/vid` : Same as `/vsong`.
├ `/deezer` : Download songs via deezer.
├ `/saavn` : Download songs via saavn.
├ `/search` : Get YouTube search query.
╘══════════════════
╒════**「 Admin Commands 」**
├ `/skip` : Skips Music.
├ `/pause` : Pause Playing Music.
├ `/resume` : Resume Playing Music.
├ `/end` : Stops playing Music.
├ `/reload` : Reloads Admin List.
├ `/userbotjoin` : Assistant Joins The Group.
├ `/userbotleave` : Assistant Leaves From The Group.
╘══════════════════""",
        reply_markup=InlineKeyboardMarkup(
              [
                  [
                      InlineKeyboardButton(
                          text="🆘 Support",
                          url="https://t.me/AnteikuUnion"),
                  ],
                  [
                      InlineKeyboardButton(
                          text="➕ Add me to your Group", 
                          url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                  ],
              ],
            ),
        )

@Client.on_callback_query(filters.regex(pattern=r"del"))
async def dell_cb(_, cb):
    await cb.answer()
    await cb.message.delete()
