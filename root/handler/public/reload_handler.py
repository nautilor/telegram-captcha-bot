#!/usr/bin/env python3


# region * Imports

from typing import List
from telegram import Update, Chat, User, Message
from telegram.ext import CallbackContext, MessageHandler, Filters
from root.helper.chat_helper import retrieve_chat
from root.constant.message import ADMIN_ADDED_TO_LIST
from root.model.chat import Chat as DatabaseChat
from time import sleep

# endregion


def handle_group_reload(update: Update, context: CallbackContext):
    chat: Chat = update.effective_chat
    user: User = update.effective_user
    # extract all admins
    admins: List[int] = [member.user.id for member in chat.get_administrators()]
    # check that the user who used the command is an admin
    if user.id in admins:
        # check if the chat is stored in the database
        chat: DatabaseChat = retrieve_chat(chat.chat_id)
        if chat:
            # add the admin only if it's not present
            if not user.id in chat.admins:
                chat.admins.append(user.id)
                message: Message = context.bot.send_message(chat.id, ADMIN_ADDED_TO_LIST)
                sleep(3)
                message.delete()


# handler for the reload command in a public chat
reload_command_handler = MessageHandler(
    Filters.chat_type.groups & Filters.command & Filters.regex("^/reload$"),
    handle_group_reload,
)