from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    friends = User.get_all()
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route('/users/new')
def new_page():
    return render_template("create_user.html")

@app.route('/create', methods=["POST"])
def create():
    user_info = request.form
    if User.is_valid_user(user_info):
        User.save(user_info)
        print('PASS')
        return redirect('/')
    print('FAIL')
    return redirect('/users/new')