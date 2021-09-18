import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

punctuation = '.,?!/\():;'

def getKeyWords(text, sw, N):
    words = word_tokenize(text)
    sw_indices = []

    uniqueWords = []
    for word in words:
        if word not in sw and word not in punctuation:
            uniqueWords.append(word)
    uniqueWords = np.unique(np.array(uniqueWords))

    matrix = np.zeros((len(uniqueWords), len(uniqueWords)))

    for i, w in enumerate(uniqueWords):
        for t, word in enumerate(words):
            if word == w:
                matrix[i, i] = matrix[i, i] + 1
                if t > 0 and words[t - 1] not in sw:
                    j = np.where(uniqueWords == words[t - 1])
                    matrix[i, j] = matrix[i, j] + 1
                if t < len(words) - 1 and words[t + 1] not in sw:
                    j = np.where(uniqueWords == words[t + 1])
                    matrix[i, j] = matrix[i, j] + 1

    matrix = np.array(matrix)

    degree = np.power(np.sum(matrix, 1), np.ones(len(uniqueWords)) * 1)
    frequency = np.diagonal(matrix)

    score = np.divide(degree, frequency)

    rankedInds = np.argsort(score)
    rankedUniqueWords = uniqueWords[rankedInds]

    return rankedUniqueWords[-N:]