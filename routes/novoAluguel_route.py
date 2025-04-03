from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import current_user
from forms import AluguelForm
from datetime import datetime
from models.db import db
from models.casa_models import Casas
from models.aluguel_models import Aluguel

novoAluguel_route_bp = Blueprint('novoAluguel_route', __name__)

@novoAluguel_route_bp.route('/novoAluguel', methods=['GET', 'POST'])
def novoAluguel():
    form = AluguelForm()
    form.casa.choices = [(casa.id, casa.nome_casa) for casa in Casas.query.all()]

    if request.method == 'POST':
        print("Dados do formulário:", form.data)  # Debug
        print("Erros:", form.errors)  # Debug

        if form.validate_on_submit():
            print("Formulário válido!")  # Debug
            aluguel = Aluguel(
                id_usuario=current_user.id,
                id_casa=form.casa.data,
                qtd_hosp=form.quantidade_pessoas.data,
                obs=form.observacoes.data,
                data_inicio=form.data_inicio.data
            )
            try:
                db.session.add(aluguel)
                db.session.commit()
                flash('Aluguel cadastrado com sucesso!', 'success')
                return redirect(url_for('home_route.home'))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao cadastrar aluguel: {str(e)}', 'danger')

    return render_template('novoAluguel.html', form=form)