from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL
from models.User import db, Usuario
from models.Tarea import Tarea
from models.Proyect import Proyecto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)