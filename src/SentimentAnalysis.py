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
import NLP_PT
import ExtractNamedEntities

# ## INITIALIZATIONS

# tokenizer for portuguse language
token = NLP_PT.tokenizerPT()

# tagger for portuguse language
tagger = NLP_PT.POStagChunk()

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
    return NewDic
                
def personSentimenti(listSent, sentilex):
    """ find in a proximity of a named entitie words negative/neutral/positive that are
    probably related with that person """
    pol = 0
    size = 0
    for i, li in enumerate(listSent):
        if li[1] == "NE":
            j = i
            j = j + 1
            for k in range(j, j+5):
                try:
                    if listSent[k][0] in sentilex:
                        pol = pol + int(sentilex[listSent[k][0]])
                        size = size + 1
                except:
                    continue
            j = i
            j = j - 3
            for k in range(j, j+5):
                if listSent[k][0] in sentilex:
                    pol = pol + int(sentilex[listSent[k][0]])
                    size = size + 1
            if size > 0:
                value = round(float(pol)/float(size))
                if value == 1:
                    print li[0], " : ", "POSITIVE"
                if value == -1:
                    print li[0], " : ", "NEGATIVE"
                if value == 0:
                    print li[0], " ; ", "NEUTRAL"
                else:
                    continue
            else:
                continue
            size = 0
            
            
#  ### AUXILIAR FUNCTIONS
def createPOSdict(text):
    """ creates a dictionary with all the words of a text postagged with floresta treebank
    and substitues previous searched named entities by "NE" 
    @input a text, string 
    @returns values from a dictionary with index as key and a tuple with word and postag as value"""
    tagdict = {}
    wordslist = token.compound_tokenizeEN(text)
    wordsdict = token.special_tokenizerEN(text)
    tagwords = tagger.florestaPOStag_aubt(encodeISO(wordslist))
    for i, tag in enumerate(tagwords):
        if tag not in tagdict:
            tagdict.update({i : (tag[0].decode('latin-1'),tag[1].decode('latin-1'))})  
    final = ExtractNamedEntities.retrievePersonalities(text, 1)
    for fi in final:
        fi = fi.split()
        for i,f in enumerate(fi):
            if i == 0:
                index0 = wordsdict[f]
                stra = f
            if i > 0:
                stra = stra + ' ' + ''.join(f)
                index = wordsdict[f]
                if index in tagdict:
                    tagdict.pop(index)
        tagdict[index0] = (stra, "NE")
    return tagdict.values()

def encodeISO(lista):
    """ encode to latin-1 a list """
    new = []
    for l in lista:
        new.append(l.encode('latin-1'))
    return new




         
    