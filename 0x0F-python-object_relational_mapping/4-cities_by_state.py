#!/usr/bin/python3
'''
Lists all citiess
'''
import sys
import MySQLdb


if __name__ == "__main__":
    userd = sys.argv[1]
    passd = sys.argv[2]
    db_name = sys.argv[3]
    connection = MySQLdb.connect(host="localhost", port=3306, user=userd,
                                 password=passd, db=db_name, charset="utf8")

    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM `cities`\
                   JOIN `states` ON state_id=states.id ORDER BY cities.id")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    connection.close()
