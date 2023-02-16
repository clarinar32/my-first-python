import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db succesfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(2,'Claris',20,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (3,'Erik',30,'bunyore')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (4,'Ian',45,'kabarak')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (5,'Pavan',32,'emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (7,'Lexi',43,'emobilis')")

conn.commit()
print("record added successfully")
conn.close()

