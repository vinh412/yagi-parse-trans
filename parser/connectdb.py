import mysql.connector

def connectdb():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0412",
    database="yagi"
  )
  return mydb