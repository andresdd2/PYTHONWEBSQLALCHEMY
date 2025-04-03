from flask_sqlalchemy import SQLAlchemy

db = SQLALchemy()

class Proyecto(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable = False)
    tareas = db.relationship('Tarea', backref="tarea", lazy=True)