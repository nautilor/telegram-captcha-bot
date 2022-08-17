#!/usr/bin/env python3

# region * Imports

from os import environ
from telegram import ChatPermissions

# endregion

TOKEN = environ.get("TOKEN", None)


NEW_MEMBER_PERMISSIONS: ChatPermissions = ChatPermissions(can_send_messages=False)

APPROVED_USER_PERMISSIONS: ChatPermissions = ChatPermissions(
    can_send_messages=True,
    can_send_other_messages=True,
    can_invite_users=True,
    can_send_polls=True,
    can_send_media_messages=True,
    can_add_web_page_previews=False,
    can_pin_messages=False,
    can_change_info=False,
)
