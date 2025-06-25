#create a database

import mysql.connector
from mysl.connector import errorcode

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

cursor = mydb.cursor()

try:
    #create the database if none exist
    cursor.execute("""
               CREATE DATABASE IF NOT EXISTS alx_book_store
               """)
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print (f"Error: {e}")

finally:
    cursor.close()
    connection.close()

