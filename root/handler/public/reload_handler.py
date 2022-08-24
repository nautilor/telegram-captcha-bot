#!/usr/bin/env python3


# region * Imports

from typing import List
from telegram import Update, Chat, ChatMember, User
from telegram.ext import CallbackContext, MessageHandler, Filters

from root.constant.message import GROUP_ADDED_TO_LIST

# endregion


def handle_group_reload(update: Update, context: CallbackContext):
    chat: Chat = update.effective_chat
    user: User = update.effective_user
    admins: List[int] = [member.user.id for member in chat.get_administrators()]
    if user.id in admins:
        # TODO: check if the group already exists and if not add it to the list
        context.bot.send_message(chat.id, GROUP_ADDED_TO_LIST)


# handler for the start command in a private chat
reload_command_handler = MessageHandler(
    Filters.chat_type.groups & Filters.command & Filters.regex("^/reload$"),
    handle_group_reload,
)