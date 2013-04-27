#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Process the stored news and discovere mentions to Portuguese politicians
Search: for each news item -> list of mentioned personalities.
#!/usr/bin/python
# -*- coding: UTF-8 -*-

Examples of News Feeds

DN: http://feeds.dn.pt/DN-Politica
JN: http://feeds.jn.pt/JN-Politica

- not worry about duplicate news from different newspapers

'''
import nltk

filename="personalities.txt"

def isPersonalitie(name):
    with open(filename, 'r') as f:
        personalities=eval(f.read())
        p = personalities['listPersonalities']
        for key in p:
            if name in key:
                return True
        return False

def extract_entities(text):
    returnlist = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node') and chunk.node=="PERSON":
                returnlist.append(' '.join(c[0] for c in chunk.leaves()))
    return returnlist

def finalPersonalities(text):
    finallist = []
    persons = extract_entities(text)
    for person in persons:
        if isPersonalitie(person):
            finallist.append(person)
    return finallist
            

def extractall_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            print chunk
            
    

def main():
    
    text = "As mais recentes exibicoes do Cavaco com a camisola encarnada nao tem passado despercebidas a ninguem, e, segundo a imprensa holandesa, o Peter e o mais recente interessado nos servicos do extremo internacional argentino, de 25 anos."
    #extractall_entities(text)
    #coisa = extract_entities(text)
    #print coisa
    coisa = finalPersonalities("Aníbal Cavaco Silva")
    print coisa
    
    #coisa = isPersonalitie('Aníbal Cavaco Silva')
    #print coisa
    
   
    

main()