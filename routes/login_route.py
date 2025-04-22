from flask import Blueprint, request, flash, redirect, url_for, session, render_template
from werkzeug.security import check_password_hash
from models import usuario_models
from flask_login import login_user

login_route_bp = Blueprint('login_route', __name__)

@login_route_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if not valida_campos(email, senha):
            return redirect(url_for('login_route.login'))
        usuario = usuario_models.Usuario.query.filter_by(email=email).first()
        if not usuario or not check_password_hash(usuario.senha, senha):
            flash('Email ou senha inválidos', 'danger')
            return redirect(url_for('login_route.login'))

        login_user(usuario)
        session['id'] = usuario.id
        return redirect(url_for('home_route.home'))
    return render_template('login.html')

def valida_campos(email, senha):
    if not email or not senha:
        flash('Preencha todos os campos do formulário', 'danger')
        return False
    return True
