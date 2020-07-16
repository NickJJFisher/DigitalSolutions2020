import sqlite3


#Create Name of database
database = "Company.db"
#Establish connection, /create new database.
conn = sqlite3.connect(database)

#Create table called Customers
conn.execute('''DROP TABLE IF EXISTS Customers;''')

#Create table with primary key, fields and datatypes
conn.execute('''CREATE TABLE Customers
            (Id INT PRIMARY KEY NOT NULL,
            Name VARCHAR(255) NOT NULL,
            Dob VARCHAR(255) NOT NULL);''')

#Enter values into table
conn.execute('''INSERT INTO Customers (Id, Name, Dob) VALUES(1234, 'Sinclair', '2018-01-11');''')
conn.execute('''INSERT INTO Customers (Id, Name, Dob) VALUES(2345, 'Fisher', '2018-04-05');''')
conn.execute('''INSERT INTO Customers (Id, Name, Dob) VALUES(3456, 'Olufson', '2018-06-10');''')

#Commit changes to databse // save changes
conn.commit()

#Close the connection
conn.close()