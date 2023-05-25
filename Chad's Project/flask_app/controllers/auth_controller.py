from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.controllers import booking_controller, listing_controller
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/login', methods=['GET'])
def login_form():
    return render_template("auth/login.html")


@app.route('/login', methods=['POST'])
def login_authenticate():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login')
    
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect("/booking/my_booking")


@app.route("/sign_up", methods=["GET"])
def register_form():
    return render_template("auth/create_user.html")


@app.route("/sign_up", methods=["POST"])
def create_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "email": request.form["email"],
        "first_name": request.form['first_name'],
        "last_name": request.form["last_name"],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    return redirect("/booking/my_booking")


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/login')