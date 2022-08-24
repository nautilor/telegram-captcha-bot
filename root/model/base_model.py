#!/usr/bin/env python3

# region * Imports

from datetime import datetime
from mongoengine import Document, DateTimeField, QuerySetManager

# endregion

class BaseModel(Document):
    
    objects = QuerySetManager()
    meta = {"allow_inheritance": True, "abstract": True}
    creation_date = DateTimeField(default=datetime.now)
