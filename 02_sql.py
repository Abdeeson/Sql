# INSERT Command 

# Import the sqlite3 library
import sqlite3 

#Create the connection object
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL command
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 840)")

cursor.execute("INSERT INTO population VALUES('San Francisco', 'SA', 800)")

#Commit the changes
conn.commit()

# Close the database
conn.close()