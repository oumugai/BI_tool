#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:15:28 2017

@author: yuya
"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/upload',methods=['POST'])
def upload():
    the_file = request.files['the_file']
    the_file.save("./" + the_file.filename)
    print(request.form['other_data'])
    return ""

if __name__  == '__main__':
    app.run()



