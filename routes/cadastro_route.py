from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.db import db
from models.usuario_models import Usuario
from werkzeug.security import generate_password_hash
from flask_login import login_user

cadastro_route_bp = Blueprint('cadastro_route', __name__)

def valida_campos(nome, email, senha, telefone, confirma_senha):
    verifica_email = Usuario.query.filter_by(email=email).first()
    if verifica_email:
        flash('Email já cadastrado!', 'danger')
        return False

    verifica_telefone = Usuario.query.filter_by(telefone=telefone).first()
    if verifica_telefone:
        flash('Telefone já cadastrado!', 'danger')
        return False

    if senha != confirma_senha:
        flash('As senhas não coincidem!', 'danger')
        return False

    if not nome or not email or not telefone or not senha:
        flash('Preencha todos os campos do formulário', 'danger')
        return False
    return True

@cadastro_route_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        #telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

        if valida_campos(nome, email, senha, 2, confirma_senha):
            senha = generate_password_hash(request.form['senha'])
            usuario = Usuario(nome, email, telefone, senha)
            db.session.add(usuario)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash('Erro no cadastro', 'danger')

            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login_route.login'))

    return render_template('cadastro.html')