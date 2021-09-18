#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:55:09 2021

@author: Alex
"""


import requests
import json

url = "https://sis.jhu.edu/api/classes/Whiting%20School%20of%20Engineering?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"

req = requests.get(url)
contents = req.json()

# Want a set for course nums
course_nums = set()

# A dictionary for al the contents
info = {}


# Get all the corse numbers to look for the section info 
for i in contents:
    department = False
    term = False
    
    if (i['Department'] == 'EN Applied Mathematics & Statistics' 
        or i['Department'] == 'EN Biomedical Engineering'
        or i['Department'] == 'Chemical and Biomolecular Engineering'
        or i['Department'] == 'Civil Engineering'
        or i['Department'] == 'Computer Engineering'
        or i['Department'] == 'Computer Science'
        or i['Department'] == 'Electrical and Computer Engineering'
        or i['Department'] == 'Electrical Engineering'
        or i['Department'] == 'Engineering Mechanics' 
        or i['Department'] == 'Environmental Engineering'
        or i['Department'] == 'General Engineering'
        or i['Department'] == 'Materials Science and Engineering'
        or i['Department'] == 'Mechanical Engineering'):   
        
        department = True
    if (i['Term'])   
    
    if (i['Department']=='EN Applied Mathematics & Statistics') and (i['Term'] == 'Fall 2021')and ('Undergraduate' in  i['Level']):
        temp = i['OfferingName'].replace('.',"")
        temp = temp + '01'
        course_nums.add(temp)
 
# COnvert array to lsit    
course_nums = list(course_nums)       



for i in course_nums:
    # Get URL of each class
    url = "https://sis.jhu.edu/api/classes/" + i + "/?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"
    req = requests.get(url)  
    
    # Conts will include information about all semesters of the course
    conts = req.json()
    
    # j will be information from the last semester
    j = conts[-1]
    # Get the section details in k in order to index
    k = j['SectionDetails'][0]
    
    temp = [j["Title"],k['Prerequisites'], k["CoRequisites"],k["Description"]]
    info[i] = temp
 
    
        
print(info) 
print(len(info))   
print(len(course_nums))



