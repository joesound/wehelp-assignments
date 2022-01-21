
#套件引入
from flask import Flask, render_template, request, session, redirect, url_for



#自己的工具
from auth import auth_user #驗證使用者帳號密碼



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('member'))  
        return render_template("home.html")
    

@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':                   #確認request方法
        account = request.values.get('account')    #取得使用者帳號
        password = request.values.get('password')  #取得使用者密碼
        auth_index, information_auth = auth_user(account, password)  #驗證使用者
        if auth_index:
            session['username'] = account
            return redirect(url_for('member'))  #驗證成功，回傳成功頁面
        else:
            return redirect(url_for('error', error_message = information_auth))   #驗證失敗，回傳失敗頁面
    else:
        return redirect(url_for('error', error_message = "No support GET method"))



#成功導向的路徑
@app.route("/member")
def member():
    if 'username' in session:
        print(request.cookies)
        return render_template("member.html") 
    else:
        return redirect(url_for('error', error_message = "You must sigin first"))

#錯誤導向的路徑
@app.route('/error')
def error():
    information_auth = request.args['error_message']
    return render_template("error.html", error_message = information_auth) 

#登出導向的路徑
@app.route('/signout')
def signout():
    session.pop('username', None)
    print(session)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=3000)

