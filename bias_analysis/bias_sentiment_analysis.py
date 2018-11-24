import nltk.classify
import os
from lexical_dict import dict_load



# define training base
def build_training_base ():
    pos = []
    neg = []
    training_base = []
    word_dict = dict_load ()
    
    for p in word_dict[0]:
        pos.append ((p, 'pos'))

    for n in word_dict[1]:
        neg.append ((n, 'neg'))
    
    training_base = pos + neg

    return training_base

def polarity_analysis():
    neg = 0
    pos = 0 
    frase = 'Eu não gosto de mentirosos'
    training_base = build_training_base()
    print(training_base)
    classifier = nltk.classify.NaiveBayesClassifier.train(training_base)
    

polarity_analysis()
