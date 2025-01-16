from flask import render_template, request, redirect, url_for
from database import SessionLocal
from models import User

def register_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        session = SessionLocal()
        try:
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                #create and save new users
                new_user = User(username=username, password=password)
                session.add(new_user)
                session.commit()

                return redirect(url_for('sucess'))
            return render_template("register.html")
        finally:
            session.close()
    

    @app.route('/success')
    def sucess():
        return 'Usuario cadastrador com sucesso'