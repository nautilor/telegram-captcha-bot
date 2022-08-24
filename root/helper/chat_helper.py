#!/usr/bin/env python3

# region * Imports

from root.model.chat import Chat

# endregion

def create_chat(chat_id: int):
    try:
        Chat(chat_id=chat_id, admins=[], join_message="").save()
    except Exception as e:
        print(f"Unable to create chat: {e}")

def retrieve_chat(chat_id: int):
    try:
        return Chat.objects().get(chat_id=chat_id)
    except Exception as e:
        print(f"Unable to find the chat with id [{chat_id}]: {e}")