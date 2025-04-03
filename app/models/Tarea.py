from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarea(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    pryecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable = False)