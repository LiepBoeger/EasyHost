from flask import Blueprint, render_template
from flask_login import login_required

from models.aluguel_models import Aluguel
from models.casa_models import Casas
from models.db import db
from models.usuario_models import Usuario

home_route_bp = Blueprint('home_route', __name__)

@home_route_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    alugueis = db.session.query(
        Aluguel,
        Casas.nome_casa.label('casa_nome'),
        Casas.foto_casa.label('casa_imagem'),
        Usuario.nome.label('usuario_nome')
    ).join(
        Casas, Aluguel.id_casa == Casas.id
    ).join(
        Usuario, Aluguel.id_usuario == Usuario.id
    ).order_by(
        Aluguel.data_inicio.desc()
    ).all()

    print(alugueis)

    return render_template('home.html', alugueis=alugueis)

