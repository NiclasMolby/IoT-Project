import mysql.connector
import time

mydb = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7291043",
  passwd="2v7AHjd8Jb",
  database="sql7291043"
)

def get_movement_data():
  mycursor = mydb.cursor()
  sql = "SELECT drinking, timestamp FROM movement"
  mycursor.execute(sql)

  result = mycursor.fetchall()
  print(len(result))
  jsonList = []
  for x in result:
    jsonList.append({
      "mode": x[0],
      "timestamp": x[1]
    })
  mydb.commit()
  mycursor.close()
  return jsonList

def insert_movement_data(data):
    mycursor = mydb.cursor()
    sql = "INSERT INTO movement (cup, drinking, timestamp) VALUES (%s, %s, %s)"
    val = ("1", data, time.time())
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")