
'''
Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse
'''

import logging
import telegram as t

import html
class CustomUser(t.User):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


    @property
    def full_name_html(self) -> str:
        """
        this will use full name as a html escaped so that if any < > will present in the
        user name it will use it as normal string
        """
        real_name = self.full_name
        escaped_name = html.escape(real_name)
        return escaped_name


    @property
    def full_name_cap(self):
        real_name = self.full_name_html
        cap_name = real_name.upper()
        cap_name = cap_name[::-1]
        return cap_name
    
    @property
    def name_double(self): #added this in start fun
        real_name = self.full_name_html
        dob = 2*(real_name)
        return dob
    
    @property
    def name_char_count(self): #use id start to checking purpose
        real_name = self.full_name_html
        leng = len(real_name)
        return leng
    
    @property
    def full_name_cap(self): #edit the existing full_name peroperyt
        real_name = self.full_name
        real_name = real_name.upper()
        real_name = html.escape(real_name)
        return real_name
    
    @property
    def double_string(self): #This can use for /start
        """
        - "Rana" becomes "RRaannaa"
        """
        input_string = self.full_name
        doubled_characters = []
        for char in input_string:
            doubled_characters.append(char * 2)
        doubled_string = ''.join(doubled_characters)
        doubled_string = html.escape(doubled_string)
        return doubled_string


# as i said before any imports
t._message.User = CustomUser

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





async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (f"Full Name Inbuild: <b><u>{user.full_name_html}</u></b>\n")
    text += (f"Full Name Cap <b><u>{user.full_name_cap}</u></b>\n")
    text += f"Your double name is: {user.name_double}\n"
    text += f"Your name length is: {user.name_char_count}\n"
    text += f"Your Fancy Name is: {user.double_string}"
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
