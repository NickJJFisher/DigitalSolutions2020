import sqlite3
import matplotlib.pyplot as plt


names = []
life = []
#Create name of database
database = "world.db"

#Connecting to database
conn = sqlite3.connect(database)

#Query database
record = conn.execute('SELECT Name, Lifeexpectancy FROM Country WHERE name = "Australia" Order by Lifeexpectancy')

#print records
for row in record:
    names.append(row[0])
    life.append(row[1])

print(names)
print(life)

plt.bar(names, life)
plt.show()

#close
conn.close()