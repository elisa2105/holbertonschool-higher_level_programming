#!/usr/bin/python3
"""
Module States
list the states
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    user = argv[1]
    passw = argv[2]
    dbv = argv[3]

    mydb = MySQLdb.connect(host="localhost",
                           user=user,
                           passwd=passw,
                           db=dbv)

    myCursor = mydb.cursor()
    myCursor.execute("select * from states \
                     order by states.id")
    states = myCursor.fetchall()
    for state in states:
        print(state)
    myCursor.close()
    mydb.close()
