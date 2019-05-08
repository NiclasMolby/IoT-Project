import mysql.connector
import time

mydb = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7291043",
  passwd="2v7AHjd8Jb",
  database="sql7291043"
)

def insert_movement_data(data):
    mycursor = mydb.cursor()
    sql = "INSERT INTO movement (cup, drinking, timestamp) VALUES (%s, %s, %s)"
    val = ("1", data, time.time())
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")