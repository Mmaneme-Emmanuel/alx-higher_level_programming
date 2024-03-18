#!/usr/bin/python3
"""script that takes in the name of a state and list its cities as db"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name, cities.id, state.name
                    FROM cities
                    INNER JOIN states ON 
                    cities.state_id = states.id
                    WHERE states.name = %s""", (sys.argv[4],))
    row = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
