from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin , login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired , ValidationError, Length
from flask_bcrypt import Bcrypt





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'
alla = "manco style"
Lala= "mochi manco style 2.0"


Login_Manager = LoginManager()
Login_Manager.init_app(app)
Login_Manager.login_view = "login"


@Login_Manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

asdasd="sadasd"




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)  



class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4 , max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4 , max=20)], render_kw={"placeholder": "Password"})

    Submit = SubmitField("Login")


@app.route('/',methods=['GET', 'POST'])   
def home():
    form = LoginForm()
    if form.validate_on_submit():
        User = User.query.filter_by(username=form.username.data).first()
        if user:
            if Bcrypt.check_password_hash(user.password, form.password.data):
                login_user(User)
                return redirect(url_for('login'))
    return render_template('main.html', form=form)






@app.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    return render_template('prueba.html')



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
