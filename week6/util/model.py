import mysql.connector

def creat_users(name, username, password):  #args = [name, username, password] 創建新用戶
        mydb = mysql.connector.connect(     #登入資料庫
                host="localhost",
                user="root",
                password="root",
                database="website"
                )
        mycursor = mydb.cursor()            #建立cursor
        try:
                sql = "SELECT username FROM member WHERE username = %s" #sql指令先從資料庫中查詢，使用帳號是否已經存在
                val = (username,)
                mycursor.execute(sql, val)
                username_in_db = mycursor.fetchone()
                if username_in_db:
                        return False, "This username has been signup"   #如果存在就產生錯誤訊息，避免重複使用者
                else:
                        sql = "INSERT INTO member (id, name, username, password, follower_count) VALUES (%s, %s, %s, %s, %s)" #如果尚未註冊，就將新增使用者到資料庫
                        val = (None, name, username, password, 0)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        mydb.close()
                        return True, "signup sucess"                   #最後回傳註冊成功訊息
        except mysql.connector.Error as err:
                return False, "Something wrong"                        #如果資料庫異常，回傳錯誤訊息
                
        


def get_user_data(user_account, user_password):                       #獲取使用者資訊，用來登入判斷，確認使用者帳號及密碼
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="website"
                )
        mycursor = mydb.cursor()


        try:
                sql = "SELECT username, password FROM member WHERE username = %s"   #透過輸入帳號，從資料庫獲取 帳號 及 密碼
                val = (user_account,)
                mycursor.execute(sql, val)
                user_data_in_db = mycursor.fetchall()
                if user_data_in_db:                                                  #如果使用者帳號存在於資料庫就進行密碼比對
                        if user_data_in_db[0][0] == user_password:                   #如果使用者密碼與輸入密碼相符 則登入成功                                          
                                return True, "Auth sucess"                           #回傳登入訊息並轉跳頁面
                        else:
                                return False, "You account or passord need to check" #登入失敗就回傳帳號或密碼有錯誤
                else:
                        return False, "You don't have signup"                        #如果找不到使用者帳號，回傳尚未註冊
        except mysql.connector.Error as err:
                return False, "You don't have signup"



def find_user_name(user_account):
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="website"
                )
        mycursor = mydb.cursor()
        try:
                sql = "SELECT name FROM member WHERE username = %s"
                val = (user_account,)
                mycursor.execute(sql, val)
                name_in_db = mycursor.fetchall()
                if name_in_db:
                        return True, name_in_db[0][0]
                else:
                        return False, "check your account"
        
        except mysql.connector.Error as err:
                return False, "Somthing wrong"






