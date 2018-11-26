#!/usr/bin/env python
import nltk
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from lexical_dict import dict_load
from text_handling import load_text, clean_break_line
import string


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

# separa o texto em sentenças
def tokenize_text (text):
    sent = []
    for l in text:
        sl = sent_tokenize (l, language='portuguese')
        for k in sl:
            sent.append(k)
    return sent
# separa as sentenças em tokens (palavras)
def tokenize_words (text):
    words = []
    for l in text:
        words.append (word_tokenize (l))
    return words

# remove as stopwords (palavras que não agregam muito sentido)
def remove_stop_words (text, words):
    for l in text:
        for w in l:
            if (w in words) or (w in string.punctuation):
                l.remove(w)
    return text

# reduz a palavra ao radical
def stemming_words (words_cleaned):
    stemmer = nltk.stem.RSLPStemmer()
    stem_words = []
    for w in words_cleaned:
        for l in w:
            nw = stemmer.stem(l)
            stem_words.append(nw)
    return stem_words
# reduz as palavras dos arquivos de palavras com polaridade para seu radical
def stemming_words_polarity (words_polarity):
    stemmer = nltk.stem.RSLPStemmer()
    stem_words_polarity = []
    for w in words_polarity:
        nw = stemmer.stem(w)
        stem_words_polarity.append(nw)
    return stem_words_polarity

# analiza a polaridade da sentença
def polarity_analysis():
    
    # carrega em words_np duas listas o arquivo de palavras com significado respectivamente positivo e negativo da lingua portuguesa
    words_np = dict_load()

    #define stop words
    stop_words = stopwords.words('portuguese')

    # Abre e limpa o arquivo
    path_text = '../web_text_parser/web_text_parser/extracted_texts/folhasp/dilma_folha/text_1675693-quem-aguenta.txt'
    text = clean_break_line ( load_text (path_text))
    token_sents =  tokenize_text (text)
    print(text) 
    print(token_sents) 


polarity_analysis()
