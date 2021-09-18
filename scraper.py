#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:55:09 2021

@author: Alex
"""


import requests
import pandas as pd


url = "https://sis.jhu.edu/api/classes/Whiting%20School%20of%20Engineering?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"

req = requests.get(url)
contents = req.json()

# Want a set for course nums
course_nums = set()

# A dictionary for al the contents



# Get all the corse numbers to look for the section info 
for i in contents:
    department = False
    term = False
    credit = False
    
    if (i['Department'] == 'EN Applied Mathematics & Statistics' 
        or i['Department'] == 'EN Biomedical Engineering'
        or i['Department'] == 'EN Chemical and Biomolecular Engineering'
        or i['Department'] == 'EN Civil Engineering'
        or i['Department'] == 'EN Computer Engineering'
        or i['Department'] == 'EN Computer Science'
        or i['Department'] == 'EN Electrical and Computer Engineering'
        or i['Department'] == 'EN Electrical Engineering'
        or i['Department'] == 'EN Engineering Mechanics' 
        or i['Department'] == 'EN Environmental Engineering'
        or i['Department'] == 'EN General Engineering'
        or i['Department'] == 'EN Materials Science and Engineering'
        or i['Department'] == 'EN Mechanical Engineering'):   
        
        department = True
    if (i['Term'] == 'Fall 2021' 
            or i['Term'] == 'Spring 2021'):
        term = True
        
    if (not '-' in i['Credits']):
        credit = True
    
    if (department and term and credit and ('Undergraduate' in  i['Level'])):
        temp = i['OfferingName'].replace('.',"")
        temp = temp + '01'
        course_nums.add(temp)
 
# Convert array to lsit    
course_nums = list(course_nums)     

numbers = {'courseNum': course_nums}
df = pd.DataFrame(numbers)
df.to_csv('courseNums.csv') 

  
"""
url = "https://sis.jhu.edu/api/classes/" + course_nums[-1] + "/?key=XV4qXo28mAdSEzyFXQi2tty7Kp3oEvmY"
req = requests.get(url)  
    
# Conts will include information about all semesters of the course
conts = req.json()
    
# j will be information from the last semester
j = conts[-1]
# Get the section details in k in order to index
k = j['SectionDetails'][0]
    
info["courseNum"].append(course_nums[-1])
info["courseName"].append(j["Title"])
info["description"].append(k["Description"])

print(info)
"""


"""
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
    
    temp = [j["Title"],k["Description"]]
    info["courseNum"].append(i)
    info["courseName"].append(j["Title"])
    info["description"].appned(k["Description"])
 
"""    
        
#print(info) 
#print(len(info))   
#print(len(course_nums))



