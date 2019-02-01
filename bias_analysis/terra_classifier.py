import re
import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import string
from random import randrange

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

def join_sentences(text):
    res = []
    for s in text:
        #print (s)
        for w in s:
            #print (w)
            res.append(w)
    return res

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


    #text = stemming_words (text)
    text = join_sentences(text)
    #dicts = []
    feature_set = {}
    for w in text:
        feature_set[w] = True
#dict ([ (w,True)])
        #dicts.append(feature_value)
    #text = dicts
#    text = make_dict(text)
    #print ("\n\n\n\n",text)
    return [feature_set]

def shuffle_list(list):
    l = len(list)
    res = [0] * l
    for i in range(l):
        while True:
            n = randrange(0,l)
            if res[n] == 0:
               res[n] = list[i]
               break
    return res

def train_bayes():

    w_dir = os.getcwd ()
    path = w_dir + '/bayes/'

    # abre um texto a ser analisado, deveria abrir varios textos
    positive_train = open (path+'treino/positive_sentences_train.txt','r')
    neutral_train = open (path+'treino/neutral_sentences_train.txt','r')
    negative_train = open (path+'treino/negative_sentences_train.txt','r')

    # a funcao que prepara os textos recebera o texto no formato devolvido
    # pelo readlines.
    positive = positive_train.readlines ()
    neutral = neutral_train.readlines ()
    negative = negative_train.readlines ()

    # a funcao prepare text executa a remocao da quebra de linha, o tokenize das sentencas,
    # o tokenize das palavras, a remocao das stopwords em portugues e o steeming, nessa ordem.

    positive = prepare_text (positive)
    negative = prepare_text (negative)
    neutral = prepare_text (neutral)


    # nTest defina quantas sentencas serao usadas para fazer o teste. na versao atual deveria
    # ser quantos arquivos de texto.
    nTest = 12
    positive_train = add_label(positive[nTest:],'positive')
    neutral_train = add_label(neutral[nTest:],'neutral')
    negative_train = add_label(negative[nTest:],'negative')

    # define as sentencas, com label conhecido, que tem a finalidade de testar o classificador.
    # agora deveria conter os arquivos e o label correspondente. Provavelmente sera melhor usar a
    # funcao prepare text e addlabel em cada arquivo e fazer um dicionario com eles.
    positive_tests = positive[:nTest]
    neutral_tests = neutral[:nTest]
    negative_tests = negative[:nTest]

    #soma todas as sentencas de treino. elas contem o label em cada palavra e o valor true.
    train = []
    train += positive_train
    train += negative_train
    train += neutral_train

    #treino do classificador
    l = nltk.NaiveBayesClassifier.train (train)

    # labels guarda a classificação original, conhecida, observed marca o resultado do classificador
    # 
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


def analyse_texts(folder,text_list,n,m,c):
    count = 0
    soma = 0
    res = []
#    parent_list = os.listdir(folder)
    for child in text_list:
        if (count >= n) and (count < m):
            f = open(folder + child,'r')
            text = prepare_text(f.readlines())[0]
            res.append(c.classify(text))
            if (c.classify(text) == "homem"):
                pass
        count = count+1
    return res    

def train(mulher_folder, mulher_list, homem_folder, homem_list,unissex_folder,unissex_List,n):
    count = 0
#    homem_list = os.listdir(homem_folder)
#    mulher_list = os.listdir(mulher_folder)
    mulher_train = []
    homem_train = []
    unissex_train = []
    for child in mulher_list:
        if count < n:
            f = open(mulher_folder + child,'r')
            text = prepare_text(f.readlines())
            mulher_train += add_label(text,'mulher')
        else:
            break
        count = count+1

    count = 0
    for child in homem_list:
        if count < n:
            f = open(homem_folder + child,'r')
            text = prepare_text(f.readlines())
            homem_train += add_label(text,'homem')
        else:
            break
        count = count+1
    count = 0
    for child in unissex_list:
        if count < n:
            f = open(unissex_folder + child,'r')
            text = prepare_text(f.readlines())
            if count == 34:
                print (text)
            unissex_train += add_label(text,'unissex')
        else:
            break
        count = count+1

    train = []
    train += mulher_train
    train += homem_train
    train += unissex_train
    l = nltk.NaiveBayesClassifier.train (train)
    return l



path_homem = '../web_text_parser/web_text_parser/extracted_texts/terra_homem/'
path_mulher = '../web_text_parser/web_text_parser/extracted_texts/terra_mulher/'
path_unissex = '../web_text_parser/web_text_parser/extracted_texts/terra_unissex/'

homem_list = os.listdir(path_homem)
mulher_list = os.listdir(path_mulher)
unissex_list = os.listdir(path_unissex)

homem_list = shuffle_list(homem_list)
mulher_list = shuffle_list(mulher_list)
unissex_list = shuffle_list(unissex_list)

nt = 80

print (homem_list[0],mulher_list[0])
c = train(path_mulher,mulher_list, path_homem,homem_list, path_unissex, unissex_list,nt)
c.show_most_informative_features(n = 100)
labels = ["mulher"] * (130 - nt) + ["homem"] * (130 - nt) + ["unissex"] * (270 - nt)


mulher_observed = analyse_texts(path_mulher, mulher_list, nt,130,c)
homem_observed = analyse_texts(path_homem, homem_list,nt,130,c)
unissex_observed = analyse_texts(path_unissex, unissex_list, nt,270, c)
observed = mulher_observed + homem_observed + unissex_observed

#print (observed)
print (nltk.ConfusionMatrix (labels, observed))

#print ("Dilma score:", analyse_texts (path_dilma, n))
#print ("Temer score:", analyse_texts(path_temer, n))
