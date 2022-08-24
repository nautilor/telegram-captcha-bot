#!/usr/bin/env python3

# region * Imports

from root.model.base_model import BaseModel
from mongoengine import ListField, IntField, StringField
# endregion

class Chat(BaseModel):
    chat_id = IntField(required=True, unique=True)
    admins = ListField(IntField())
    join_message = StringField()