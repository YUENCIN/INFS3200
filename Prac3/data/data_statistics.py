

'''
        /*
         * Please implement the Task 1 code here, including both two sub-tasks
         */
'''

import src.oracle.DBconnect as db
from src.data.restaurant import restaurant as res


try:
    con = db.create_connection()
    cur = db.create_cursor(con)
    string_query = "SELECT CITY FROM RESTAURANT"
    cities = []
    cur.execute(string_query)
    num_new_york = 0
    num_new_york_city = 0
    for city in cur:
        cities.append(city[0])
        if city[0] == 'new york\n':
            num_new_york+=1
        if city[0] == 'new york city\n':
            num_new_york_city+=1
    cur.close()
    con.close()
    temp_c = []
    for c in cities:
        if c not in temp_c:
            temp_c.append(c)
    print('new york,', num_new_york)
    print('new york city,', num_new_york_city)
    print('Number of distinct values in city:', len(temp_c))

except:
    print("Error occurred. Statement execution failed.")