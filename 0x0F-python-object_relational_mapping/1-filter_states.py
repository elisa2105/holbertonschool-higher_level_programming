#!/usr/bin/python3
'''
Listing all states in a database that start with a N
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 password=password, db=db_name,
                                 charset="utf8")

    cursor = connection.cursor()
    cursor.execute("SELECT `id`, `name` FROM `states` WHERE `name`\
                   LIKE BINARY 'N%' ORDER BY `id` ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()
