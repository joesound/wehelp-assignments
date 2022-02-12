from flask import Flask, render_template, request, session, redirect, url_for, Blueprint

#自己的工具
from util.auth_tool import auth_user #驗證使用者帳號密碼

app_auth = Blueprint('auth', __name__)

@app_auth.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':                   #確認request方法
        account = request.values.get('account')    #取得使用者帳號
        password = request.values.get('password')  #取得使用者密碼
        auth_index, information_auth, user_name = auth_user(account, password)  #驗證使用者
        if auth_index:
            session['username'] = user_name
            return redirect(url_for('auth.member'))  #驗證成功，回傳成功頁面
        else:
            return redirect(url_for('auth.error', error_message = information_auth))   #驗證失敗，回傳失敗頁面
    else:
        return redirect(url_for('auth.error', error_message = "No support GET method"))



#成功導向的路徑
@app_auth.route("/member")
def member():
    if 'username' in session:
        return render_template("member.html", name = session['username']) 
    else:
        return redirect(url_for('auth.error', error_message = "You must sigin first"))

#錯誤導向的路徑
@app_auth.route('/error')
def error():
    information_auth = request.args['error_message']
    return render_template("error.html", error_message = information_auth) 



#登出導向的路徑
@app_auth.route('/signout')
def signout():
    session.pop('username', None)
    print(session)
    return redirect(url_for('home'))