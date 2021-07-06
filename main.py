import flask
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
#import drowsiness detection
import numpy as np


app = Flask(__name__)



@app.route('/')
@cross_origin()
def index():
    file=open(r'drowsiness detection.py', 'r').read()
    return exec(file)


#@app.route('/predict', methods=['POST'])
#@cross_origin()
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000, use_reloader=False)
