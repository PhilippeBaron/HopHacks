#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:06:58 2021

@author: Alex
"""

from flask import Flask, render_template, flash, redirect, url_for, request
from form import CourseID, ReturnButton
import requests
import getSimilarClasses

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'


@app.route("/")

@app.route("/home", methods=['GET', 'POST'])
def home():
    form = CourseID()
    if form.validate_on_submit():
        return redirect(url_for('output', course_num = form.courseID.data))
    return render_template('home.html', title = 'Main', form = form)


@app.route("/output", methods=['GET', 'POST'])

@app.route("/output/<course_num>", methods=['GET', 'POST'])
def output(course_num):
    
    ret = ReturnButton()
    
    
    course = course_num.replace('.','') + '01'
    url = "https://sis.jhu.edu/api/classes/" + course + "/?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"
    req = requests.get(url)
    conts = req.json()
    if len(conts) == 0:
        return redirect(url_for('home'))
    
    
    # j will be information from the last semester
    j = conts[-1]
    # Get the section details in k in order to index
    k = j['SectionDetails'][0]
    info = {}
    info["courseName"] = j["Title"]
    info["description"] = k["Description"]
    info["prereqs"] = k["Prerequisites"]
    
    
    classes, codes = getSimilarClasses.getSimilarClasses(course_num)
    classes_and_codes = []
    for i in range(0, len(classes)):
       classes_and_codes.append(classes[i] + ": " + codes[i])
        

    return render_template('output.html', title = 'Output',
                           course_num = course_num, info = info, button = ret,
                           classes = classes_and_codes)
    



if __name__ == '__main__':
    app.run(debug = True)