'''
This is from the https://t.me/pythontelegrambottalk/254831
'''

import logging

import telegram as t

class CustomUser(t.User):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    @property
    def full_name_cap(self):
        real_name = self.full_name
        cap_name = real_name.upper()
        cap_name = cap_name[::-1]
        return cap_name
    
    @property
    def name_double(self):
        real_name = self.full_name
        dob = 2*(real_name)
        return dob

# as i said before any imports
t._message.User = CustomUser

from telegram import Update
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode

print("DIR of new class\n", dir(CustomUser))
print("DIR of t.User\n", dir(t.User))
print(t.User == CustomUser)

def setup_logger():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)

logger = setup_logger()

async def cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await context.bot.send_message(user.id, f"{user.full_name}")
    await context.bot.send_message(user.id, f"{user.full_name_cap}")

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (f"Hello <b><u>{user.full_name}</u></b>\n")
    text = (f"Hello <b><u>{user.name_double}</u></b>\n")
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)

async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    text = f"<u>{text}</u>"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)

async def extra_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    text = f"<code>{text}</code>"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)

def main() -> None:
    application = Application.builder().token("meow").build()

    application.add_handler(CommandHandler(
        command=["start"],
        callback=start_cmd,
        filters=filters.ChatType.PRIVATE,
        block=False
    ))
    application.add_handler(CommandHandler(
        command=["cap", "help"],
        callback=cap,
        filters=filters.ChatType.PRIVATE,
        block=False
    ))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_fun))
    application.add_handler(MessageHandler(filters.Command(), extra_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()


