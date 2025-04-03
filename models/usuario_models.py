from models.db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    telefone = db.Column(db.String)
    senha = db.Column(db.String(250))

    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def get_id(self):
        return self.id

    @staticmethod
    def authenticate(email, senha):
        user = Usuario.query.filter_by(email=email).first()
        if user and user.senha == senha:
            return user

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(int(id))