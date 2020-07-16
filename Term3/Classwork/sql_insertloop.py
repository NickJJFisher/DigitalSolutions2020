import sqlite3
from guizero import App, Picture, PushButton, Window, TextBox, Text
database = "Company.db"
#Establish connection, /create new database.
conn = sqlite3.connect(database)
Background = "#00FFFF"
app = App(height= 360, width= 520, title= "Main Menu",bg= Background, layout="grid")
Idshow = []
Nameshow = []
Dobshow = []
def entervalues():
    id_input = Id_box.value
    name_input = Name_box.value
    dob_input = Date_box.value
    conn.execute("INSERT INTO Customers (Id, Name, Dob) VALUES ({0}, {1}, {2})".format(id_input, name_input, dob_input))
    Filler = Text(app, text="Success", grid=[1,2])
    # Commit changes to databse // save changes
    conn.commit()
    # Close the connection
    conn.close()
def displaytable():
    ALL = conn.execute('SELECT * FROM Customers')
    for row in ALL:
        Idshow.append(row[0])
        Nameshow.append(row[1])
        Dobshow.append(row[2])
    Showid = Text(app, text=Idshow, grid=[1,4])
    Shown = Text(app, text=Nameshow, grid=[1, 5])
    Showd = Text(app, text=Dobshow, grid=[1, 6])
Enter = PushButton(app, command=entervalues, grid=[1,2], text = "Enter")
DisplayAll = PushButton(app,command=displaytable, grid=[1,3], text= "Display All Values")
Id_box = TextBox(app, grid=[0,1])
Name_box = TextBox(app, grid=[1,1])
Date_box = TextBox(app, grid=[2,1])
Id_text = Text(app,text="ID", grid=[0,0])
Name_text = Text(app,text="Last Name", grid=[1,0])
Date_text = Text(app,text="Date of Birth", grid=[2,0])
Id_box.bg = "white"
Name_box.bg = "white"
Date_box.bg = "white"
Enter.bg = "white"
app.display()

#Create Name of database

# #Create table called Customers
# conn.execute('''DROP TABLE IF EXISTS Customers;''')
# #Create table with primary key, fields and datatypes
# conn.execute('''CREATE TABLE Customers
#             (Id TEXT PRIMARY KEY NOT NULL,
#             Name TEXT NOT NULL,
#             Dob DATE NOT NULL);''')

# enter = input("Would u like to answer some values, y/n: ")
# while enter == 'y' or enter == 'Y':
#     id_input = int(input("Enter your ID Number: "))
#     name_input = input('Enter your last name: ')
#     dob_input = input('Enter your DOB in form: YYYY-MM-DD:')
#  #Enter values into table
#     conn.execute("INSERT INTO Customers (Id, Name, Dob) VALUES ({0}, {1}, {2});".format(id_input, name_input, dob_input))
#     enter = 'F'



