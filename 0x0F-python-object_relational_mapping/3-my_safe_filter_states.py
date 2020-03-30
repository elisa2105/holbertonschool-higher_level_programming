#!/usr/bin/python3
'''
shows states but SQLinjection safe
'''
import sys
import MySQLdb


if __name__ == "__main__":
    userd = sys.argv[1]
    passd = sys.argv[2]
    db_name = sys.argv[3]
    param = sys.argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306, user=userd,
                                 password=passd, db=db_name, charset="utf8")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states` WHERE `name` = (%s)\
                  ORDER BY `id` ASC", (param,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()
