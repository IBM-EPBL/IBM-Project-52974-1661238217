import sqlite3

conn=sqlite3.connect("detail.db")
print("opened database successfully")

conn.execute('create table detail(name text,email text,phone text,password text')
print("Table created successfully")
conn.close()