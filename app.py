from flask import Flask
from routes import login_route, cadastro_route, home_route, logout_route, cadastroCasa_route, novoAluguel_route
from models.db import db
from models import usuario_models
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Registro de rotas
app.register_blueprint(cadastro_route.cadastro_route_bp)
app.register_blueprint(login_route.login_route_bp)
app.register_blueprint(home_route.home_route_bp)
app.register_blueprint(logout_route.logout_route_bp)
app.register_blueprint(cadastroCasa_route.cadastroCasa_route_bp)
app.register_blueprint(novoAluguel_route.novoAluguel_route_bp)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return usuario_models.Usuario.query.get(int(user_id))

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)