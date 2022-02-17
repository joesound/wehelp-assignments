from flask import Flask, render_template, request, session, redirect, url_for, Blueprint
import json

from api.apimodel import get_user_by_username, update_username_by_username

api_member = Blueprint('api_member', __name__, url_prefix='/api')

@api_member.route("/members" , methods=['GET','POST'])
def members():
    if request.method == "GET":
        username = request.args.get('username')
        user_data = get_user_by_username(username)
        user_index_for_query = user_data[0]
        if user_index_for_query:
            user_id, user_name, user_username= user_data[1][0], user_data[1][1], user_data[1][2]
            Udata = {
                        "data":{
                            "id":user_id,
                            "name":user_name,
                            "username":user_username,
                        }
                    }
            return json.dumps(Udata)
        else:
            Udata = {"data":"null"}   # user not found
            return json.dumps(Udata)
        
        
@api_member.route("/member" , methods=['POST'])
def update_user_name():
    if 'username' in session:
        if request.method == "POST":
            update_username_dict = json.loads(request.data)
            update_username = update_username_dict["username"]
            index, message = update_username_by_username(update_username, session['username'])
            if index:
                data = {"ok":True}
                return json.dumps(data)
            else:
                data = {"error": True}
                return json.dumps(data)
    else:
        data = {"error": True}
        return json.dumps(data)


