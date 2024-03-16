#!/usr/bin/python3
"""script that takes and displays values in state"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",user=sys.argv[1], 
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()        
