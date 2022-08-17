#!/usr/bin/env python3

# region * Imports

from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters

# endregion


def handle_private_start(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "👋 Hello and welcome,\n\nTo use me just add me as an administrator into a group and I will do the rest."
    )
    update.effective_message.delete()


private_start_handler = MessageHandler(
    Filters.chat_type.private & Filters.command & Filters.regex("^/start$"),
    handle_private_start,
)
