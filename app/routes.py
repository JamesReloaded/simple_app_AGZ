from app import app
from flask import render_template, request, jsonify
import requests
import os
import json

# Getting information from .env file for connectivity
USERNAME = str(os.environ.get('VGS_USER'))
PASSWORD = str(os.environ.get('VGS_PASS'))
TENANT_ID = str(os.environ.get('VAULT_ID'))
ENVIRONMENT = str(os.environ.get('VGS_ENV'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', VAULT_ID= TENANT_ID, VGS_ENV=ENVIRONMENT)

@app.route('/add_encryption', methods=['POST'])
def add_encryption():
    return render_template('message.html', card_number = request.form['card_number'], card_cvc = request.form['card_cvc'], card_expirationDate = request.form['card_expirationDate'])

@app.route("/forward", methods=['POST'])
def forward():
    os.environ['HTTPS_PROXY'] = "http://{}:{}@{}.{}.verygoodproxy.com:8080".format(USERNAME, PASSWORD, TENANT_ID, ENVIRONMENT)
    response = requests.post('https://echo.apps.verygood.systems/post',
                            json={
                                'card_number': request.form['card_number'],
                                'card_cvc': request.form['card_cvc'],
                                'card_expirationDate': request.form['card_expirationDate']
                            },
                            verify='sandbox.pem')
    # Getting JSON Data
    json_data = json.loads(response.json()['data'])
  
    return render_template('forward.html', 
                            card_number = json_data['card_number'],
                            card_cvc = json_data['card_cvc'], 
                            card_expirationDate = json_data['card_expirationDate']
                            )
