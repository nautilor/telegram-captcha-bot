#!usr/bin/env python3

from root.bot import start_bot
from root.helper.database_helper import db_connect

def main():
    db_connect()
    start_bot()


if __name__ == "__main__":
    main()
