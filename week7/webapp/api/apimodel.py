import mysql.connector
from util.config import SQL_USER, SQL_PASSWORD
mydb = mysql.connector.connect(     #登入資料庫
                host="localhost",
                user= SQL_USER ,
                password= SQL_PASSWORD ,
                database="website"
                )
#GET user

def get_user_by_username(username):
    
    mycursor = mydb.cursor()
    try:
        sql = "SELECT id, name, username FROM member WHERE username = %s" #sql指令先從資料庫中查詢，使用帳號是否已經存在
        val = (username,)
        mycursor.execute(sql, val)
        username_information = mycursor.fetchone()
        if username_information:
            mycursor.close
            return True, username_information, "OK get uesr_information"   #如果存在就產生錯誤訊息，避免重複使用者
        else:
            mycursor.close
            return False, False, "fail pls check uername"                   #最後回傳註冊成功訊息
    except mysql.connector.Error as err:
            mycursor.close
            return False, False, "Something wrong"                        #如果資料庫異常，回傳錯誤訊息

# UPDATE use data

def update_username_by_username(update_username, username):
    mycursor = mydb.cursor()
    print(update_username, username)
    try:
        update_name_of_user_sql =  "UPDATE member SET name = %s WHERE username = %s" #"UPDATE member AS men, (SELECT id FROM member WHERE username = %s ) AS user_id SET name= %s WHERE men.id = user_id.id" #sql指令，找出username對應的name，將name進行更新
        val = (update_username, username,)
        mycursor.execute(update_name_of_user_sql, val)
        mydb.commit()

        check_user_name_update = "SELECT name FROM member WHERE username = %s"      #將更新的name找出來,提供後續比較
        val = (username,)
        mycursor.execute(check_user_name_update, val)
        updatename_information = mycursor.fetchone()
        sql_update_name = updatename_information[0]                
        if sql_update_name == update_username:                                      #比較更新的name,如果更新成功，就回傳成功訊息
            mycursor.close
            return True, "update sucess"                                            
        else:                                                                       #如果錯誤救回傳錯誤訊息
            mycursor.close
            return False, "update fail something wrong"                           
    except mysql.connector.Error as err:
            print(err)
            mycursor.close
            return False , "Something wrong"                                        #如果資料庫異常，回傳錯誤訊息