"""
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes, Update

from AsuX import rani


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ 🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤   ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"http://t.me/{context.bot.username}?startgroup=true",
            )
        ]
    )
    await msg.reply_text(
        f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\n🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ \n",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ 🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤   ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ",
                url=f"http://t.me/{context.bot.username}?startgroup=true",
            )
        ]
    )
    await msg.reply_text(
        f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ \n\n🦋͢𝆺𝅥𓆩〭〬𝐂𖽪֟፝͢𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ͢𝆺𝅥😻⤍🖤 ᴄᴀɴ ʀᴇꜱᴛʀɪᴄᴛ ᴡʜɪᴄʜ ᴄᴏɴᴛᴀɪɴꜱ ᴘᴜʙʟɪᴄ ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


START = CommandHandler(["chatbot", "start"], start, block=False)
HELP = CommandHandler(["chelp", "help"], help, block=False)

rani.add_handler(START)
rani.add_handler(HELP)
