import mysql.connector


create_members_data = []

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="website"
)


mycursor = mydb.cursor()
sql = "INSERT INTO members (id, name, username, password, follower_count) VALUES (%s, %s, %s, %s, %s)"
val = (None, "test", "test", "test", 100)
mycursor.execute(sql, val)

mydb.commit()

