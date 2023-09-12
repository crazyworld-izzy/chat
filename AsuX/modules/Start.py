"""
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes

from AsuX import rani


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ 🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"http://t.me/{context.bot.username}?startgroup=true",
            )
        ]
    )
    await msg.reply_text(
        f"ʜᴇʏ\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nɪ'ᴍ {context.bot.first_name}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐌ʏ 𝐎ᴡɴᴇʀ  𓆩⟶‌𒌋⃝💙⋆↬ 𝐃𖽖⃨𖽴᪱𖽖‌⃮\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐎ᴡɴᴇʀ - 𝐈ᴅ : @moon_shine_dada\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐒ᴜᴘᴘᴏʀᴛ - @tamil_magical_love\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ 🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ",
                url=f"http://t.me/{context.bot.username}?startgroup=true",
            )
        ]
    )
    await msg.reply_text(
        f"ʜᴇʏ\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nɪ'ᴍ {context.bot.first_name}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐌ʏ 𝐎ᴡɴᴇʀ  𓆩⟶‌𒌋⃝💙⋆↬ 𝐃𖽖⃨𖽴᪱𖽖‌⃮\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐎ᴡɴᴇʀ - 𝐈ᴅ : @moon_shine_dada\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n𝐒ᴜᴘᴘᴏʀᴛ - @tamil_moon_shine\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


START = CommandHandler(["chatbot", "start"], start, block=False)
HELP = CommandHandler(["chelp", "help"], help, block=False)

rani.add_handler(START)
rani.add_handler(HELP)
