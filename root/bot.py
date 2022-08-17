#!/usr/bin/env python3

# region * Imports

from telegram.ext import Dispatcher, Updater
from root.constant.telegram import TOKEN
from root.handler.public.new_member_handler import (
    new_member_handler,
    captcha_button_pressed,
    member_leaving_handler,
)

from root.handler.private.start_handler import private_start_handler

# endregion


def start_bot():
    updater: Updater = Updater(TOKEN)
    add_handlers(updater.dispatcher)
    updater.start_polling(drop_pending_updates=True)


def add_handlers(dispatcher: Dispatcher):
    dispatcher.add_handler(new_member_handler)
    dispatcher.add_handler(member_leaving_handler)
    dispatcher.add_handler(captcha_button_pressed)
    # handler for the start command in a private chat
    dispatcher.add_handler(private_start_handler)
