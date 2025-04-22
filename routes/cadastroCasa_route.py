from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from models.casa_models import Casas
from models.db import db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

cadastroCasa_route_bp = Blueprint('cadastroCasa_route', __name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads', 'casas')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cadastroCasa_route_bp.route('/cadastroCasa', methods=['GET', 'POST'])
def cadastrarCasa():
    if request.method == 'POST':
        nomeCasa = request.form.get('nomeCasa')
        fotoCasa = request.files.get('fotoCasa')

        if not nomeCasa or not fotoCasa:
            flash('Preencha os dois campos', 'danger')
        else:
            if 'fotoCasa' in request.files:
                file = request.files['fotoCasa']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
                    filepath = os.path.join('static/uploads', filename)
                    fotoCasa.save(filepath)

            id_usuario = session.get('id')
            casa = Casas(id_usuario, nomeCasa, filename)
            try:
                db.session.add(casa)
                db.session.commit()
                
                flash('Residência cadastrada com sucesso', 'sucess')
                return redirect(url_for('cadastroCasa_route.cadastrarCasa'))
            except:
                db.session.rollback()
                flash('Erro ao Cadastrar residência', 'danger')
                
    return render_template('cadastroCasa.html')
