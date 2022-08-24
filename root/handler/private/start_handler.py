#!/usr/bin/env python3

# region * Imports

from telegram import Update, User
from telegram.ext import CallbackContext, MessageHandler, Filters

from root.constant.message import NEW_USER_PRIVATE_CHAT_WELCOME

# endregion


def handle_private_start(update: Update, context: CallbackContext):
    user: User = update.effective_user
    update.effective_message.reply_text(NEW_USER_PRIVATE_CHAT_WELCOME(user))
    update.effective_message.delete()


# handler for the start command in a private chat
private_start_handler = MessageHandler(
    Filters.chat_type.private & Filters.command & Filters.regex("^/start$"),
    handle_private_start,
)
