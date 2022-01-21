
#輸入(帳號及密碼)，回傳 成功失敗index, 訊息(bool, information)
def auth_user(user_account, user_password):
    if user_account == "" :                    #未輸入帳號
        return False, "account is must"     #回傳錯誤訊息
    elif user_password == "":                  #未輸入密碼
        return False, "password is must"    #回傳錯誤訊息
    else:                                      #都有輸入
        if user_account == "test" and user_password == "test": #驗證帳號密碼
            return True, "auth success"                    #驗證成功，回傳成功訊息
        
        else:
            return False, "auth fail pls check your account or password" #驗證失敗，回傳失敗訊息
