from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proyecto(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)  
    tareas = db.relationship('Tarea', backref="proyecto", lazy=True)