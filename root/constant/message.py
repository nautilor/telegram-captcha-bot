#!/usr/bin/env python3

# region * Imports

# endregion

USER_LINK = lambda user: f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"

JOIN_MESSAGE_TEXT: str = "Welcome {}, please confirm you're a human by selecting the right captcha."
JOIN_MESSAGE = lambda user: JOIN_MESSAGE_TEXT.format(USER_LINK(user))

NEW_USER_PRIVATE_CHAT_WELCOME_TEXT: str = "Hello {}, I'm a captcha bot that will filter out all userbots from your group, just add me to a group a launch the command /reload"
NEW_USER_PRIVATE_CHAT_WELCOME = lambda user: NEW_USER_PRIVATE_CHAT_WELCOME_TEXT.format(USER_LINK(user))

ADMIN_ADDED_TO_LIST: str = "You are now a bot admin of these group!"