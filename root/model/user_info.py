#!/usr/bin/env python3

# region * Imports

from dataclasses import dataclass

# endregion


@dataclass
class UserInfo:
    user_id: int
    chat_id: int
    message_id: int
    captcha_text: str
