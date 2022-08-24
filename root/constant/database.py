#!/usr/bin/env python3

# region * Imports

from os import environ

# endregion

DBUSERNAME = environ.get("DBUSERNAME", "")
DBPASSWORD = environ.get("DBPASSWORD", "")
DBHOST = environ.get("DBHOST", "")
DBDATABASE = environ.get("DBNAME", "")
DBPORT = int(environ.get("DBPORT", "27017"))