#!/usr/bin/env python3

# region * Imports

from typing import List
from telegram import Update, User, Message
from telegram import InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup
from telegram.ext import CallbackContext, MessageHandler, Filters
from telegram.ext import ConversationHandler, CallbackQueryHandler
from root.constant.captcha import CAPTCHA_LENGTH
from root.constant.telegram import APPROVED_USER_PERMISSIONS, NEW_MEMBER_PERMISSIONS
from root.helper.captcha_helper import generate_image_data, generate_random_string
from random import shuffle

from root.model.user_info import UserInfo

# endregion

USER_CAPTCHA = {}


def build_new_member_keyboard(captcha_text: str):
    keyboard = []
    # Generate some fake options
    options: List[str] = [generate_random_string() for _ in range(0, 5)]
    # Add the right option to the list of possible options
    options.append(captcha_text)
    # Shuffle the options to give them always a different order
    shuffle(options)
    # Create the keyboard
    for line in zip(options[0:3], options[3:6]):
        keyboard.append(
            [
                Button(button, callback_data="authorize_{}".format(button))
                for button in line
            ]
        )
    return Markup(keyboard)


def store_user_information(
    user_id: int, chat_id: int, message_id: int, captcha_text: str
):
    global USER_CAPTCHA
    USER_CAPTCHA[user_id] = UserInfo(user_id, chat_id, message_id, captcha_text)


def handle_new_members(update: Update, context: CallbackContext):
    chat_id: int = update.effective_chat.id
    # Extract the list of new users that joined the group
    users: List[User] = update.effective_message.new_chat_members
    for user in users:
        # Generate a random captcha for the user validation
        captcha_text: str = generate_random_string()
        # Generate the keyboard for the user to validate itself
        keyboard: Markup = build_new_member_keyboard(captcha_text)
        # Generate a picture from the captcha text
        captcha_image = generate_image_data(captcha_text)
        text: str = f"Please {user.first_name} CONFIRM the captcha"
        # Send the captcha along with the keyboard for every new users
        message: Message = context.bot.send_photo(
            chat_id, captcha_image, caption=text, reply_markup=keyboard
        )
        # Store the information to confirm them later
        store_user_information(user.id, chat_id, message.message_id, captcha_text)
        # Restrict the user permissions
        context.bot.restrict_chat_member(chat_id, user.id, NEW_MEMBER_PERMISSIONS)


def confirm_new_member_captcha(update: Update, context: CallbackContext):
    global USER_CAPTCHA
    # Answer the callback to remove the loading icon from the button
    update.callback_query.answer()
    # Get the generated code
    callback_data: str = update.callback_query.data.split("_")[-1]
    user_id: int = update.effective_user.id
    chat_id: int = update.effective_chat.id
    # Retrieve the user information stored in memory
    user_info: UserInfo = USER_CAPTCHA.get(user_id, None)
    if not user_info:
        # Another user presses the button

        return
    if user_info.captcha_text == callback_data:
        # Now the user can send messages normally since it has been verified
        context.bot.restrict_chat_member(chat_id, user_id, APPROVED_USER_PERMISSIONS)
        # Delete the captcha message
        update.effective_message.delete()
        # Remove the information of the user cause they are not needed anymore
        del USER_CAPTCHA[user_id]
        # Stop the conversation


def handle_member_leaving(update: Update, context: CallbackContext):
    return ConversationHandler.END


# handler for new members joining the group
new_member_handler = MessageHandler(
    Filters.chat_type.groups & Filters.status_update.new_chat_members,
    handle_new_members,
)

# handler for when a user press a button
captcha_button_pressed = CallbackQueryHandler(
    pattern="^authorize_\w{%s}$" % CAPTCHA_LENGTH,
    callback=confirm_new_member_captcha,
)

# handler for when a user leave the group
member_leaving_handler = MessageHandler(
    Filters.chat_type.groups & Filters.status_update.left_chat_member,
    handle_member_leaving,
)