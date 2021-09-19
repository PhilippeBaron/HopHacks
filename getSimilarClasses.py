import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial  import distance as dist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity as cos_sim
from getKeyWords import getKeyWords as gkw
from sklearn.neighbors import KDTree
from sklearn.gaussian_process.kernels import Matern, RBF,  ConstantKernel
import networkx as nx
import csv

stopwords = np.load('stopwords.npy')

def getData():
    
    descriptions = pd.read_csv('courseInfo.csv')
    

    descriptions = descriptions[descriptions.description.notnull()]


    desc1 = list(descriptions['description'].values)
    course_name1 = list(descriptions['courseName'].values)
    course_cod1 = list(descriptions['courseNum'].values)

    #print(course_name1)    

    return desc1, course_name1, course_cod1


def filtering(c):
    return list(gkw(c[0], stopwords, 20))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def getSimilarClasses(code, range1=5,
                      a=0.5, b=0.2, c=0.3):
    courseDescriptions, courseNames, courseCodes = getData()
    
    classIndex = 0
    for i in range(0, len(courseCodes)):
        if courseCodes[i] == code:
            classIndex = i
    
    #classIndex = np.where(courseCodes==code)
  
    
    desc_all = ['']
    title_all = ['']

    N_samples = len(courseDescriptions)
    feedback=np.zeros([N_samples, N_samples])
    #print(range(N_samples))
    for i in range(0, N_samples):
        desc_all += filtering([courseDescriptions[i]])
        title_all += filtering([courseNames[i]])

    desc_all = desc_all + title_all
    desc_all = np.unique(desc_all)

    vectorizer = CountVectorizer()
    vectorizer.fit(desc_all)
    vocc = vectorizer.vocabulary_

    Vectors = np.zeros([N_samples, len(vocc)])
    for i in range(N_samples):
        Vectors[i, :] = vectorizer.transform([courseDescriptions[i]]).toarray().ravel()

    K1 = cos_sim(Vectors)
    K1_nod = K1 - np.eye(N_samples)
    D = np.sum(K1_nod, axis=1)
    D_inv = np.diag(1.0 / (D))
    K1_norm = D_inv @ K1_nod

    Vectorst = np.zeros([N_samples, len(vocc)])

    for i in range(N_samples):
        Vectorst[i, :] = vectorizer.transform([courseNames[i]]).toarray().ravel()

    K1t = cos_sim(Vectorst)
    K1_nodt = K1t - np.eye(N_samples)
    Dt = np.sum(K1_nodt, axis=1)
    D_invt = np.diag(1.0 / (Dt + 1E-6))
    K1_normt = D_invt @ K1_nodt

    FS = a * K1_nod + b * sigmoid(feedback) + c * K1_nodt
    


    sortedIndices = np.argsort(FS[classIndex, :])
    
    
    courseNames = np.array(courseNames)
    courseNames = courseNames[sortedIndices]
    
    courseCodes = np.array(courseCodes)
    courseCodes = courseCodes[sortedIndices]


    return courseNames[-range1:], courseCodes[-range1:]

#classes = getSimilarClasses('EN.530.327')
#print(classes)

