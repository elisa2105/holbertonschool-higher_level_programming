#!/usr/bin/python3
"""
Module State
lists all cities
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]
    paramstate = argv[4]

    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    myCursor = mydb.cursor()
    sql = "select cities.name from cities\
           inner join states on cities.state_id = states.id\
           where states.name = %s\
           order by cities.id asc"
    myCursor.execute(sql, (paramstate,))
    cities = myCursor.fetchall()
    c = ", ".join(city[0] for city in cities)
    print(c)
    myCursor.close()
    mydb.close()
