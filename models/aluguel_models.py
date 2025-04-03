from models.db import db
from flask_login import UserMixin

class Aluguel(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_casa = db.Column(db.Integer, db.ForeignKey('casas.id'))
    qtd_hosp = db.Column(db.Integer)
    data_inicio = db.Column(db.DateTime)
    obs = db.Column(db.String)

    def __init__(self, id_usuario, id_casa, qtd_hosp, data_inicio, obs):
        self.id_usuario = id_usuario
        self.id_casa = id_casa
        self.qtd_hosp = qtd_hosp
        self.data_inicio = data_inicio
        self.obs = obs
