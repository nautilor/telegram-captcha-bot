#!/usr/bin/env python3

# region * Imports

from mongoengine import connect
from pymongo import MongoClient
from root.constant.database import DBDATABASE, DBHOST, DBPASSWORD, DBUSERNAME, DBPORT
# endregion

def db_connect():
    try:
        client = connect(DBDATABASE, username=DBUSERNAME, password=DBPASSWORD, host=DBHOST, port=DBPORT)
        client.server_info()
    except Exception as e:
        print(f"* Unable to establish the connection with the database: {e}")