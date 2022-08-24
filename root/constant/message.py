#!/usr/bin/env python3

# region * Imports

from typing import Callable
from telegram import User

# endregion

USER_LINK: Callable[[User]] = lambda user: f"<a href=tg://user?id={user.id}>{user.first_name}</a>"

JOIN_MESSAGE: str = "Welcome {}, please confirm you're a human by selecting the right captcha."
JOIN_MESSAGE: Callable[[User]] = lambda user: JOIN_MESSAGE.format(USER_LINK(user))

NEW_USER_PRIVATE_CHAT_WELCOME: str = "Hello {}, I'm a captcha bot that will filter out all userbots from your group, just add me to a group a launch the command /reload"
NEW_USER_PRIVATE_CHAT_WELCOME: Callable[[User]] = lambda user: NEW_USER_PRIVATE_CHAT_WELCOME.format(USER_LINK(user))

GROUP_ADDED_TO_LIST: str = "The group has now been added succesfully!"