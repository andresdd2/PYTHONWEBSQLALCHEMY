from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):  # Capitalize 'Model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proyectos = db.relationship('Proyecto', backref="usuario", lazy=True)