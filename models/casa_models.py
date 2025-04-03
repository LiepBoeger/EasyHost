from models.db import db
from flask_login import UserMixin

class Casas(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    nome_casa = db.Column(db.String)
    foto_casa = db.Column(db.String)

    def __init__(self, id_usuario, nome_casa, foto_casa):
        self.id_usuario = id_usuario
        self.nome_casa = nome_casa
        self.foto_casa = foto_casa
