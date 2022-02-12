from util.model import get_user_data #登入時判斷使用者是否存在於資料庫 及 密碼是否正確



#輸入(帳號及密碼)，回傳 成功失敗index, 訊息(bool, information)
def auth_user(user_account, user_password):
    if user_account == "" :                    #未輸入帳號
        return False, "account is must", False     #回傳錯誤訊息
    elif user_password == "":                  #未輸入密碼
        return False, "password is must", False    #回傳錯誤訊息
    else:
        auth_index ,user_name ,message = get_user_data(user_account, user_password)    #驗證帳號密碼
        if auth_index:
            return True, message, user_name                    #驗證成功，回傳成功訊息及使用者名稱
        
        else:
            return False, message, user_name #驗證失敗，回傳失敗訊息

#創建新帳戶，用於確認輸入資訊是否缺少，後續會加上判斷，避免使用者輸入惡意語法
def auth_creat_account(user_name, user_account, user_password):
    if user_name == "":
        return False, "name is must"
    elif user_account == "":
        return False, "account is must"
    elif user_password == "":
        return False, "password is must"

    else:
        return True, "information collect success"