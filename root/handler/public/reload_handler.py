#!/usr/bin/env python3


# region * Imports

from typing import List
from telegram import Update, Chat, User, Message
from telegram.ext import CallbackContext, MessageHandler, Filters
from root.helper.chat_helper import add_admin, retrieve_chat
from root.constant.message import ADMIN_ADDED_TO_LIST
from time import sleep

# endregion


def handle_group_reload(update: Update, context: CallbackContext):
    chat: Chat = update.effective_chat
    user: User = update.effective_user
    # extract all admins
    admins: List[int] = [member.user.id for member in chat.get_administrators()]
    # check that the user who used the command is an admin
    if user.id in admins:
        # add the new admin to the chat
        add_admin(chat.id, user.id)
        # send a confirmation  message
        message: Message = context.bot.send_message(chat.id, ADMIN_ADDED_TO_LIST)
        sleep(3)
        # delete the confirmation message
        message.delete()


# handler for the reload command in a public chat
reload_command_handler = MessageHandler(
    Filters.chat_type.groups & Filters.command & Filters.regex("^/reload$"),
    handle_group_reload,
)