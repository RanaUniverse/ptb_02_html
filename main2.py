
'''
This code is also runnable, i made this with the purpose of checking how to add
the USER Class new property in my code without chage the source code of  PTB
This is my main file to run all things are connected mainly with all things

Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''

import sys
sys.dont_write_bytecode = True

import logging

from telegram import Update, User
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters


from telegram.ext import ContextTypes


from telegram.constants import (ParseMode)

'''
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Below will my special coding started
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
'''

def setup_logger():
    '''this is basic to show if the bot has started or not'''
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)

logger = setup_logger()



class CustomUser(User):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    @property
    def full_name_cap(self):
        '''Returns capitalized name with end to first'''
        real_name = self.full_name
        cap_name = real_name.upper()
        cap_name = cap_name[::-1]
        return cap_name

User = CustomUser


async def cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This will come when /cap will come to bot and then 
    it will return the cap name to user
    '''
    user = update.message.from_user
    await context.bot.send_message(user.id, f"{user.full_name}")
    await context.bot.send_message(user.id, f"{user.full_name_cap}")










async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This fun is execute when a user send /start to the bot in private
    This will reply to user by calling his name with some bold or underline formatting 
    for more impressive showing i will show the error what happens when executes this
    '''
    user = update.message.from_user
    text = (f"Hello <b><u>{user.full_name_html}</u></b>\n")
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


    
async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This funcion will trigger when a user will send a text to bot
    the work of the function will it will just add a underline to the
    text user will send to bot,
    like if user will send Rana Universe bot will send Rana Universe with underline
    so i will use html tag here easily with <u> </u>'''
    ...
    user = update.message.from_user
    text = update.message.text
    text = f"<u>{text}</u>"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)




async def extra_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This fun will trigger and it will send all the text including the args
    and send it back to user with a mono code block so that it can copy
    '''
    user = update.message.from_user
    text = update.message.text
    text = f"<code>{text}</code>"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
    







def main() -> None:
    """Start the bot."""

    application = Application.builder().token("Token🍌🍌🍌).build()

    application.add_handler(CommandHandler(
        command= ["start"],
        callback= start_cmd,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["cap", "help"],
        callback= cap,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_fun))
    application.add_handler(MessageHandler(filters.Command(), extra_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()







