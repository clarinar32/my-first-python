import sqlite3
conn=sqlite3.connect('Cities.db')
data=conn.execute("select * from Cities")
for row in data:
    print ("ID=",row[0])
    print ("NAME=",row[1])
    print ("RESIDENTS=",row[2])
    print ("LOCATION=",row[3], "\n")
conn.close()