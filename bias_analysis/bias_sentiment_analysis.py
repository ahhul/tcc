import re
import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import string

# define training base
def build_training_base  ():
    pos = []
    neg = []
    training_base = []
    word_dict = dict_load  ()
    
    for p in word_dict[0]:
        pos.append  ( (p, 'pos'))

    for n in word_dict[1]:
        neg.append  ( (n, 'neg'))
    
    training_base = pos + neg

    return training_base

def make_dict(texts):
    dicts = []
    for s in texts:
        feature_value = dict ([ (word,True) for word in s])
        dicts.append(feature_value)
    return dicts

def add_label(text,label):
    train = [(featureset,label) for featureset in text]
    return train


def tokenize_words  (text):
    words = []
    for l in text:
        s = word_tokenize (l)
        words.append  (s)
    return words

def remove_stop_words  (text, words):
    cleaned_words = []
    for l in text:
        nl = []
        for w in l:
            if  (w in words) or  (w in string.punctuation):
                continue
            else:
                nl.append (w)
        cleaned_words.append (nl)
    return cleaned_words

def stemming_words  (words_cleaned):
    stemmer = nltk.stem.RSLPStemmer ()
    stem_words = []
    for l in words_cleaned:
        nl = []
        for w in l:
            nw = stemmer.stem (w)
            nl.append (nw)
        stem_words.append (nl)
    return stem_words

def tokenize_text  (text):
    sent = []
    for l in text:
        sl = sent_tokenize  (l, language='portuguese')
        for k in sl:
            sent.append (k)
    return sent


def clean_break_line  (text_lines):
    re_break = re.compile  (r'\\n')
    clean_text = []
    for l in text_lines:
        new_line = l.strip ()
        re.sub (re_break, "", new_line)
        
        if new_line != '':
            clean_text.append (new_line)
        
    return clean_text


def prepare_text (text):
        
    # carrega em words_np duas listas o arquivo de palavras com significado respectivamente positivo e negativo da lingua portuguesa

    #define stop words
    text = clean_break_line (text)
    text = tokenize_text (text)
    stop_words = stopwords.words ('portuguese')


    #token_sents =  tokenize_text  (text)
    text = tokenize_words (text)

    text = remove_stop_words (text, stop_words)


    text = stemming_words (text)
    text = make_dict(text)

    return text


def train_bayes():

    w_dir = os.getcwd ()
    path = w_dir + '/bayes/'


    positive_train = open (path+'treino/positive_sentences_train.txt','r')
    neutral_train = open (path+'treino/neutral_sentences_train.txt','r')
    negative_train = open (path+'treino/negative_sentences_train.txt','r')

    positive = positive_train.readlines ()
    neutral = neutral_train.readlines ()
    negative = negative_train.readlines ()

    #stop_words = stopwords.words ('portuguese')

    positive = prepare_text (positive)
    negative = prepare_text (negative)
    neutral = prepare_text (neutral)
    #print positive
    # positive = tokenize_words (positive)
    # negative = tokenize_words (negative)
    # neutral = tokenize_words (neutral)
    # remove_stop_words (positive,stop_words)
    # remove_stop_words (negative,stop_words)
    # remove_stop_words (neutral,stop_words)


    nTest = 12
    positive_train = add_label(positive[nTest:],'positive')
    neutral_train = add_label(neutral[nTest:],'neutral')
    negative_train = add_label(negative[nTest:],'negative')

    positive_tests = positive[:nTest]
    neutral_tests = neutral[:nTest]
    negative_tests = negative[:nTest]

    train = []
    train += positive_train
    train += negative_train
    train += neutral_train


    l = nltk.NaiveBayesClassifier.train (train)


    labels = []
    observed = []

    for s in positive_tests:
        t = dict ([ (word,True) for word in s])
        c = l.classify (t)
        labels.append ('positive')
        observed.append (c)


    for s in neutral_tests:
        t = dict ([ (word,True) for word in s])
        c = l.classify (t)
        labels.append ('neutral')
        observed.append (c)


    for s in negative_tests:
        t = dict ([ (word,True) for word in s])
        c = l.classify (t)
        labels.append ('negative')
        observed.append (c)

    print (nltk.ConfusionMatrix (labels, observed))
    print ([nltk.ConfusionMatrix (labels, observed)])
    return l


def analyse_texts(folder,n):
    count = 0
    soma = 0
    parent_list = os.listdir(folder)
    for child in parent_list:
        if count < n:
            f = open(folder + child,'r')
            text = prepare_text(f.readlines())
            for s in text:
                res = c.classify(s)
                if res == 'positive':
                    soma += 1
                elif res == 'negative':
                    soma -= 1       
        else:
            break
        count = count+1
    return soma    


c = train_bayes()
path_temer = '../web_text_parser/web_text_parser/extracted_texts/folhasp/michel_folha/'
path_dilma = '../web_text_parser/web_text_parser/extracted_texts/folhasp/dilma_folha/'

n = 1000
print ("Dilma score:", analyse_texts (path_dilma, n))
print ("Temer score:", analyse_texts(path_temer, n))
