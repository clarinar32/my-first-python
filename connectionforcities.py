import sqlite3
conn=sqlite3.connect('Cities.db')
print("opened db succesfully")

conn.execute("INSERT INTO Cities(ID,NAME, RESIDENTS,LOCATION) VALUES(26,'Nairobi','one m','Kenya')")
conn.execute("INSERT INTO Cities(ID,NAME, RESIDENTS,LOCATION)VALUES (36,'Dar esalam','one m','Tanzania')")
conn.execute("INSERT INTO Cities(ID,NAME, RESIDENTS,LOCATION)VALUES (46,'Djibouti','one m','Djibouti')")
conn.execute("INSERT INTO Cities(ID,NAME, RESIDENTS,LOCATION)VALUES (56,'Lusaka','one m','Zambia')")
conn.execute("INSERT INTO Cities(ID,NAME, RESIDENTS,LOCATION)VALUES (76,'Arusha','one m','Tanzania')")

conn.commit()
print("record added successfully")
conn.close()

