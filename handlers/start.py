# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✣ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan Bergabung dengan Grup kita \'✨Republic Friends✨\' tekan ombol di bawah untuk bergabung ke Official Group Kita.\n\n✣ Untuk Memulai Starz Music Bot anda bisa menambahkan [Assistant Starz Music](https://t.me/StarzMusicAssistant) ke grup Anda untuk memutar musik di obrolan suara grup Anda,Dan jadikan saya mempunyai akses admin.\n\nManaged With ☕️ By [Rezy](https://t.me/ItsmeAlsya)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "✨ Republic Friends✨", url="https://t.me/Republicfriend")
                  ],[
                    InlineKeyboardButton(
                        "My Master", url="https://t.me/ItsmeAlsya"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/gabutannyaumat"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/Republicfriend"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/ItsmeAlsya"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/Republicfriend"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/ItsmeAlsya"
                    )
                ]
            ]
        )
   )
