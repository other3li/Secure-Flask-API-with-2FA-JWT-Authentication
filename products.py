# products.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import mysql

products = Blueprint('products', __name__)

@products.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.json
    name = data['name']
    description = data['description']
    price = data['price']
    quantity = data['quantity']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)", 
                   (name, description, price, quantity))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Product added successfully'}), 201

@products.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()

    return jsonify(products)
