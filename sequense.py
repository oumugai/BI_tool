#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:47:34 2017

@author: yuya
"""
import pandas as pd
from flask import Flask, render_template, request
from werkzeug import secure_filename
from sklearn.decomposition import PCA
transformed = None
read_data   = None
app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/pca', methods = ['GET', 'POST'])
def pca_file():
    
    #主成分分析する
    pca =PCA(n_components=2)
    pca.fit(read_data)

    #分析結果を元にデータセットを主成分に変換
    transformed = pca.fit_transform(read_data)    
    
    return render_template('main.html',name=range(2) , message=transformed)


@app.route('/upload',methods =['GET','POST'])
def uploaded_file():
    if request.method == 'POST':
       f = request.files['file']
       f.save(secure_filename(f.filename))
       read_data = pd.read_csv(f.filename)
  
    return render_template('main.html',column=read_data.columns , message=read_data)     

if __name__ == "__main__":
    app.run()