import mysql.connector

SHOW_DATABSES = "SHOW DATABASES"
SELECT_TABLES = "SELECT TABLES"


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS `website`")
mycursor.execute("USE website")
mycursor.execute("CREATE TABLE IF NOT EXISTS `website`. `member`(id bigint PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL,username varchar(255) NOT NULL,password varchar(255) NOT NULL,follower_count int DEFAULT 0,time datetime DEFAULT CURRENT_TIMESTAMP())")
















# sql_creat_table = """ 
#                         id bigint PRIMARY KEY AUTO_INCREMENT,
      
#                         name varchar(255) NOT NULL,
      
#                         username varchar(255) NOT NULL,

#                         password varchar(255) NOT NULL,
      
#                         follower_count int DEFAULT 0,
        
#                         time datetime DEFAULT CURRENT_TIMESTAMP()
                        
#                         """
# mycursor.execute("CREATE TABLE members" + "(" + sql_creat_table + ")")










# try:
#     mycursor.execute("CREATE DATABASE website")

# except mysql.connector.Error as err:
#     print("Something went wrong: {}".format(err.errno))
#     pass





