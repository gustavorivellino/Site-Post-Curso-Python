from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '6b5c188c0719ed391875284f3add42dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_criar_conta'
login_manager.login_message = 'Faça login para ter acesso ao usuários !'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes