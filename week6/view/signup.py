from flask import Flask, render_template, request, session, redirect, url_for, Blueprint

#自己的工具
from util.model import creat_users            #新增帳戶使用
from util.auth_tool import auth_creat_account #判斷註冊帳號是否有意缺少資訊等
app_signup = Blueprint('signup', __name__)
CREAT_USER_URL = "http://127.0.0.1:3000/api/members"



@app_signup.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    
    if request.method == 'POST': #新增使用者
        name = request.values.get('name')    #取得使用者名稱
        account = request.values.get('username')    #取得使用者帳號
        password = request.values.get('password')  #取得使用者密碼
        auth_index, information_auth = auth_creat_account(name, account, password)
        if auth_index:
            user_data = {"name":name, "account":account, "password":password}
            signup_index, message = creat_users(user_data["name"], user_data["account"], user_data["password"])
            if signup_index:
                return redirect(url_for('home'))  
            else:
                return redirect(url_for('auth.error', error_message = message))
        else:
            return redirect(url_for('auth.error', error_message = information_auth))
            