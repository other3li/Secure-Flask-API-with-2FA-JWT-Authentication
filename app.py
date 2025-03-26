# app.py

from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from db import init_db
from auth import auth
from products import products

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
init_db(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(products, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
