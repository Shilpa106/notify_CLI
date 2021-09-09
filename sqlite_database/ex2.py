import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn . cursor ()
#create the salesman table 
cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")

# inserting data into the table
cursor . execute ( """
INSERT INTO salesman(salesman_id,'name', 'city',commission)
VALUES(5001,'James Hoog', 'New York', 0.15)
""")
cursor . execute ( """
INSERT INTO salesman(salesman_id,'name', 'city',commission)
VALUES(5002,'Nail Knite', 'Paris', 0.25)
""")
cursor . execute ( """
INSERT INTO salesman(salesman_id,'name', 'city',commission)
VALUES(5003,'Pit Alex', 'London', 0.15)
""")
cursor . execute ( """
INSERT INTO salesman(salesman_id,'name', 'city',commission)
VALUES(5004,'Mc Lyon', 'Paris', 0.35)
""")
conn.commit ()
print ( 'Data entered successfully.' )
conn . close ()

if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")