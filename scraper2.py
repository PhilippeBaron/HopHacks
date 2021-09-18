#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:10:26 2021

@author: Alex
"""

import requests
import pandas as pd


info = {}

info["courseNum"] = []
info["courseName"] = []
info["description"] = []


course_nums = pd.read_csv("courseNums.csv")

nums = course_nums.loc[:,"courseNum"]



for i in nums:
    url = "https://sis.jhu.edu/api/classes/" + i + "/?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"
    req = requests.get(url)  
        
    # Conts will include information about all semesters of the course
    conts = req.json()
    
    # j will be information from the last semester
    j = conts[-1]
    # Get the section details in k in order to index
    k = j['SectionDetails'][0]

    
    
    info["courseNum"].append(i)
    info["courseName"].append(j["Title"])
    info["description"].append(k["Description"])
    
df = pd.DataFrame(info)
df.to_csv('courseInfo.csv')     

