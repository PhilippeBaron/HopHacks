#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:47:08 2021

@author: Alex
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,ValidationError

def validate_course_num(form, field):
    if len(field.data) != 10:
        raise ValidationError('Course Number must be 10 charactrs long')
    elif field.data[0:2] != 'EN':
        raise ValidationError('Course suffix incorrect')
    elif field.data[2] != '.' and field.data[6] != '.':
        raise ValidationError('Invalid format')
    elif not field.data[3:6].isnumeric():
        raise ValidationError('Invalid format')
    elif not field.data[7:10].isnumeric():
        raise ValidationError('Invalid format')    

class CourseID(FlaskForm):
    courseID = StringField('Course Number',
                           validators = [DataRequired(), validate_course_num])
    submit = SubmitField('Enter')

class ReturnButton(FlaskForm):
    submit = SubmitField('Enter')
    
    