#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:47:34 2017

@author: yuya
"""
import pandas as pd
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
       f = request.files['file']
       f.save(secure_filename(f.filename))
       read_data = pd.read_csv(f.filename)
       
       return render_template('main.html',name=read_data.columns, message=read_data)

if __name__ == "__main__":
    app.run()
