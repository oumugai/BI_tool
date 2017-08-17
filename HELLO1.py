#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:15:28 2017

@author: yuya
"""
# app.py
@app.route('/')
def index():
    #template/index.html  のテンプレートを使う
    #message という変数にHelloと代入した状態でテンプレート内で使う
    return render_template('index.html',message="Hello")