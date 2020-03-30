#!/usr/bin/python3
"""
Lists all cities in a given state
"""
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
    cursor.execute("SELECT cities.name FROM `cities` JOIN `states`\
                   ON cities.state_id=states.id LIKE BINARY %s\
                   ORDER BY cities.id ASC", (param,))
    cities = cursor.fetchall()
    print(', '.join([i[0] for city in cities]))
    cursor.close()
    connection.close()
