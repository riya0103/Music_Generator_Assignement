import sqlite3
import datetime

conn = sqlite3.connect("log.db")
conn.execute("create table employee (name text, timestamp timestamp)")
conn.close()

conn = sqlite3.connect("log.db")
c = conn.execute("select * from employee")
conn.commit()
c.description
c.close()
conn.close()

conn = sqlite3.connect("log.db")
c = conn.cursor()
name = "aa"
timestamp = datetime.datetime.now()
c.execute("insert into employee (name, timestamp) values(?,?)",(name,timestamp))
conn.commit()
c.close()
conn.close()

conn = sqlite3.connect("log.db")
c = conn.execute("select * from employee")
for row in c:
    print(row)

c.close()
conn.close()

