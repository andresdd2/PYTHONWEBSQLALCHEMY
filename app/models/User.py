from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    proyectos = db.Relationship('Proyecto', backref="usuario", lazy=True)