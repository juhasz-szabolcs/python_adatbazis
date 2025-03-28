import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
#általunk létrehozott adatbázis
DATABASE = "mydatabase"

# táblázat létrehozása
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

# adatbázisok mutatása
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# adatbázis használata
mycursor.execute(f"USE {DATABASE}")

# táblázat létrehozása
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# adatok beszúrása (INSERT)