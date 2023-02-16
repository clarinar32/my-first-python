import sqlite3
conn=sqlite3.connect('Cities.db')
print("opened db successfully")
conn.execute("CREATE TABLE Cities"
             "(ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "RESIDENTS TEXT NOT NULL,"
             "LOCATION TEXT NOT NULL)")

print("Table for cities successfully created")
conn.close()
