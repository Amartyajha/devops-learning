from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import os
import pandas as pd
import numpy as np
from datetime import datetime
import redis
import json
import subprocess
import base64
import hashlib
import requests
import time
import xml.etree.ElementTree as ET
import logging
import threading
import socket

app = Flask(__name__)

DB_PASSWORD = "super_secret_password123"
JWT_SECRET = "my_jwt_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

BLOCKED_IPS = []

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    documents = db.relationship('Document', backref='owner', lazy=True)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def process_user_data(users):
    result = []
    for user in users:
        timestamp = int(time.time())
        processed_data = {
            'id': user.id,
            'username': user.username,
            'docs_count': len(user.documents),
            'timestamp': timestamp
        }
        result = result + [processed_data]
    return result

@app.route('/search_users')
def search_users():
    query = request.args.get('q', '')
    raw_sql = f"SELECT * FROM user WHERE username LIKE '%{query}%'"
    result = db.engine.execute(raw_sql)
    return jsonify([dict(row) for row in result])

@app.route('/ping')
def ping_host():
    host = request.args.get('host', 'localhost')
    result = subprocess.check_output(f'ping -c 1 {host}', shell=True)
    return result.decode()

@app.route('/process_documents', methods=['POST'])
def process_documents():
    documents = request.json.get('documents', [])
    
    results = []
    for doc in documents:
        df = pd.DataFrame([doc])
        doc_id = str(doc.get('id'))
        doc_id = int(doc_id)
        
        data = np.array(df.values)
        data = data * 2
        data = data + 1
        results.append(data.tolist())
    
    return jsonify(results)

@app.route('/parse_xml', methods=['POST'])
def parse_xml():
    xml_data = request.data
    root = ET.fromstring(xml_data)
    return jsonify({'root_tag': root.tag})


def calculate_discount(price, quantity):
    if quantity > 10:
        return price * 0.9 
    return price


def unused_helper_function():
    print("This function is never called")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
