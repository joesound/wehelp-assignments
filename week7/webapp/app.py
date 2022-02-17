
#套件引入
from flask import Flask, render_template, request, session, redirect, url_for, Blueprint


from view.auth import app_auth
from view.signup import app_signup
from api.members import api_member

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.register_blueprint(app_auth)
app.register_blueprint(app_signup)

app.register_blueprint(api_member)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('auth.member'))  
        return render_template("home.html")


if __name__ == '__main__':
    app.run(port=3000, debug=True)

