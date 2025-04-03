from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from models.casa_models import Casas
from models.db import db
from werkzeug.utils import secure_filename
import os

cadastroCasa_route_bp = Blueprint('cadastroCasa_route', __name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads', 'casas')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cadastroCasa_route_bp.route('/cadastroCasa', methods=['GET', 'POST'])
def cadastrarCasa():
    if request.method == 'POST':
        nomeCasa = request.form['nomeCasa']
        fotoCasa = request.form['fotoCasa']

        if not nomeCasa or not fotoCasa:
            flash('Preencha os dois campos', 'danger')
        else:
            if 'foto_casa' in request.files:
                file = request.files['foto_casa']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                    file.save(os.path.join(UPLOAD_FOLDER, filename))

            id_usuario = session.get('id')
            casa = Casas(id_usuario, nomeCasa, fotoCasa)
            db.session.add(casa)
            db.session.commit()
            return redirect(url_for('cadastroCasa_route.cadastrarCasa'))
    return render_template('cadastroCasa.html')
