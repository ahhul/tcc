# -*- coding: utf-8 -*-
import nltk
import os
import re

# Lê o dicionário léxico ReLi-Lex para armazenar palavras com polaridade positivas e negativas
def dict_load ():
    path = os.path.dirname ('ReLi-Lex/')
    list_files = os.listdir (path)
    positive_words = []
    negative_words = []

    re_positive = re.compile (r'Positivos')
    re_negative = re.compile (r'Negativos')
    re_word = re.compile ('\w+')

    for i in list_files:
        if (i[-10] == 'i'):
            new_path = os.path.join (path, i)
            with open (new_path, 'r', encoding = "ISO-8859-1") as f: 
                lines = f.readlines()
                for l in lines:
                    positive_words.append(l[1:-2])
        else:
            new_path = os.path.join (path, i)
            with open (new_path, 'r', encoding = "ISO-8859-1") as f: 
                lines = f.readlines()
                for l in lines:
                    negative_words.append(l[1:-2])
    
    return positive_words, negative_words

def read_train_set (path)
    pass
dict_load()
