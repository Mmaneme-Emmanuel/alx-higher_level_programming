#!/usr/bin/python3
"""script that lists all cities from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    sql_query = "SELECT * FROM cities ORDER BY id ASC"
    cur.execute(sql_query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
