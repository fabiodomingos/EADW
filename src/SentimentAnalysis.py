#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Determine , for each entity (entity means personality) found, in each news item:
- if the news item contains options on that entity
- if it does, whether that sentiment is positive, negative or neutral

'''
# IMPORTS
import nltk.data
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords

## # MAIN FUNCTIONS

def qualifyNew(words, sentilex):
    """ intersect words from a sentimental analysis db like sentilex
    with the words from the input text and qualify the input text
        @input: words - from an input text in a list format, each entry one word 
                sentilex - sentimental analysis in python dictionary format 
        @returns: String "NOTICIA POSITIVA" for a positive text
                  String "NOTICIA NEGATIVA" for a negative text
                  String "NOTICIA NEUTRA"   for a neutral text  """
    keys=words.intersection(sentilex)
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
    
    
def extractSentilex(Sentilex):
    sentilexDic={}
    with open(Sentilex, 'r') as f:
        for line in f:
            lineWords=line.split(';')
            palavra=lineWords[0].split('.')[0]
            sentimento=lineWords[2].split('=')[1]
            sentilexDic.update({palavra:sentimento})
    return sentilexDic
    

## invocar o qualify new sobre uma lista de palavras do texto total mas tambem de uma sentence.
## criar uma db com os politicos e o numero de ocorreuncias positivas e negativas a medida que colecta
## na mesma funcao fazer postag com o floresta ou mac morpho e filtro apenas de adjectivos e so isso e que identifica o mood quanto a pessoa
## para a noticia e utilizado tudo. conta-se o nr de palavras de uam frase e o numero de adjectivos positivos e negativos deppis normaliza-se com
## uma formula
            


         
    