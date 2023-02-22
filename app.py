import time
import redis
from flask import Flask, render_template, jsonify
import psycopg2
import json

import databse_control


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/get_json_data')
def get_json_data():
    with open('static/data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/save_to_db')
def save_to_db():
    try:
        databse_control.save_json_to_table("static/data.json")
        return "success"

    except Exception as e:
        return str(e)



if __name__ == '__main__':

    databse_control.save_json_to_table("static/data.json")
    app.run()