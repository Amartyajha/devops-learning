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

# Unused imports (dead code)
import logging
import threading
import socket

app = Flask(__name__)

# Security Issue: Hardcoded credentials
DB_PASSWORD = "super_secret_password123"
JWT_SECRET = "my_jwt_secret_key"

# Security Issue: Insecure database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Inefficient data structure: Using list instead of set for O(n) lookup
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

# Performance Issue: Unnecessary computation in loop
def process_user_data(users):
    result = []
    for user in users:
        # Inefficient: Recalculating same value in loop
        timestamp = int(time.time())
        processed_data = {
            'id': user.id,
            'username': user.username,
            'docs_count': len(user.documents),
            'timestamp': timestamp
        }
        # Unnecessary list conversion
        result = result + [processed_data]
    return result

# Security Issue: SQL Injection vulnerability
@app.route('/search_users')
def search_users():
    query = request.args.get('q', '')
    # NEVER do this in real code - SQL injection vulnerability
    raw_sql = f"SELECT * FROM user WHERE username LIKE '%{query}%'"
    result = db.engine.execute(raw_sql)
    return jsonify([dict(row) for row in result])

# Security Issue: Command Injection vulnerability
@app.route('/ping')
def ping_host():
    host = request.args.get('host', 'localhost')
    # NEVER do this in real code - Command injection vulnerability
    result = subprocess.check_output(f'ping -c 1 {host}', shell=True)
    return result.decode()

# Performance Issue: Inefficient data processing
@app.route('/process_documents', methods=['POST'])
def process_documents():
    documents = request.json.get('documents', [])
    
    # Inefficient: Creating new DataFrame for each document
    results = []
    for doc in documents:
        df = pd.DataFrame([doc])
        # Unnecessary type conversion
        doc_id = str(doc.get('id'))
        doc_id = int(doc_id)
        
        # Memory inefficient: Creating new array for each operation
        data = np.array(df.values)
        data = data * 2
        data = data + 1
        results.append(data.tolist())
    
    return jsonify(results)

# Security Issue: XML parsing vulnerability
@app.route('/parse_xml', methods=['POST'])
def parse_xml():
    xml_data = request.data
    # NEVER do this in real code - XML parsing vulnerability
    root = ET.fromstring(xml_data)
    return jsonify({'root_tag': root.tag})

# Business Logic Error: Incorrect calculation
def calculate_discount(price, quantity):
    # Error: Applies discount incorrectly
    if quantity > 10:
        return price * 0.9  # Should be (price * quantity) * 0.9
    return price

# Dead Code: Never used function
def unused_helper_function():
    print("This function is never called")

# Security Issue: Insecure password hashing
def hash_password(password):
    # NEVER do this in real code - Use proper password hashing
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == '__main__':
    # Security Issue: Debug mode in production
    app.run(debug=True, host='0.0.0.0', port=5000)
