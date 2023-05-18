from database import db

class Usuario(db.Model):
  __tablename__ = "usuario"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100))
  email =  db.Column(db.String(100))
  senha = db.Column(db.String(100))

  def __init__(self, nome, email, senha):
    self.nome= nome
    self.emai= email
    self.senha= senha

  def __repr__(self):
    return '<Usuário{}>'.format(self.nome)
