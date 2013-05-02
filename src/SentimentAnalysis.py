#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Determine , for each entity (entity means personality) found, in each news item:
- if the news item contains options on that entity
- if it does, whether that sentiment is positive, negative or neutral

'''
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize 
import nltk.data
from nltk.tokenize import word_tokenize 
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.corpus import floresta

def ExtractSentilex(Sentilex):
    sentilexDic={}
    with open(Sentilex, 'r') as f:
        for line in f:
            lineWords=line.split(';')
            palavra=lineWords[0].split('.')[0]
            sentimento=lineWords[2].split('=')[1]
            sentilexDic.update({palavra:sentimento})
    return sentilexDic

def FilterNew(text):
    portuguese_stops = stopwords.words('portuguese')
    STOPS=portuguese_stops+['.',',',':',';','-']
    NewTokenizer=sent_tokenizerPT(text)
    Filtro=[]
    for sentence in NewTokenizer:
        WordsList=word_tokenizePT(sentence, 'TB')
        FiltroSentence=[word for word in WordsList if word not in STOPS]
        Filtro=Filtro+FiltroSentence
    return set(Filtro)

def QualifyNew(palavras, sentilex):
    keys=palavras.intersection(sentilex)
    NewDic={k:sentilex[k] for k in keys}
    positivo=0
    negativo=0
    for k in NewDic:
        if NewDic[k]=='1':
            positivo=positivo+1
        elif NewDic[k]=='-1':
            negativo=negativo+1
        else:
            continue
    if positivo>negativo: print "NOTICIA POSITIVA"
    elif negativo>positivo: print "NOTICIA NEGATIVA"
    else: print "NOTICIA NEUTRA"
    
            
## This is the sent_tokenizer in PT
def sent_tokenizerPT(text):
    tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
    return tokenizer.tokenize(text) # return sentence's list       

def word_tokenizePT(sentence, tokenizer):
    """ tokenize a sentence in words
        @input params: sentence - a sentence, a phrase
                       tokenizer - "TB" for TreebankWord
                                   "WP" for WordPunct
        @returns word's list or error """
    if tokenizer == "TB":
        tokenizerTB = TreebankWordTokenizer() 
        return tokenizerTB.tokenize(sentence)
    elif tokenizer == "WP":
        tokenizerWP = WordPunctTokenizer()
        return tokenizerWP.tokenize(sentence)
    else:
        return "error"   
            

#text="Olá mundo. Bom ver-te. Obrigado por comprar este livro, o meu chocolate é bom. A puta é uma venenoso com sida"
#QualifyNew(FilterNew(text),ExtractSentilex(Sentilex))

         
    