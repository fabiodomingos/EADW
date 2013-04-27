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

personalities={}

filename="personalities.txt"

with open(filename, 'r') as f:
    personalities=eval(f.read())
    

def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node') and chunk.node=="PERSON":
                print chunk.node, ' '.join(c[0] for c in chunk.leaves())

def extractall_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            print chunk
            
    

def main():
    text = "As mais recentes exibicoes de Cavaco com a camisola encarnada nao tem passado despercebidas a ninguem, e, segundo a imprensa holandesa, o ACMilan e o mais recente interessado nos servicos do extremo internacional argentino, de 25 anos."
    extractall_entities(text)

main()