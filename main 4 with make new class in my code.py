


import logging

from telegram import Update
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode


def setup_logger():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)

logger = setup_logger()



class NewUserProperty:

    def __init__(self, user) -> None:
        pass
    @property
    def full_name_cap(self):
        real_name = self.full_name
        cap_name = real_name.upper()
        cap_name = cap_name[::-1]
        return cap_name
    
    @property
    def name_double(self): #added this in start fun
        real_name = self.full_name
        dob = 2*(real_name)
        return dob

    @property
    def name_char_count(self): #use id start to checking purpose
        real_name = self.full_name
        leng = len(real_name)
        return leng
    
    @property
    def full_name11(self): #edit the existing full_name peroperyt
        if self.last_name:
            full_n = f"{self.first_name} {self.last_name}"
            return full_n.upper()
        return self.first_name









async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    new_user = NewUserProperty(user)
    text = (f"Hello <b><u>{user.full_name}</u></b>\n")
    # text = (f"Hello <b><u>{new_user.full_name_11}</u></b>\n")
    text += f"Hello Your double name is: {new_user.name_double}\n"
    text += f"Your name length is: {new_user.name_char_count}\n"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)



async def cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await context.bot.send_message(user.id, f"{user.full_name}")
    await context.bot.send_message(user.id, f"{user.full_name_cap}")



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
    application = Application.builder().token("🍌🍌🍌").build()

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
