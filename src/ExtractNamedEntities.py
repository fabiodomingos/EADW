#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Process the stored news and discover mentions to Portuguese politicians
Search: for each news item -> list of mentioned personalities.

'''
# ## imports
import nltk
import NLP_PT # our lib for Natural Language Processing according to Portuguese Language



# ## INITIALIZATIONS

# file with personalities and his famous level according to Sapo
filename="personalities.txt"

# instance of NLP_PT
token = NLP_PT.tokenizerPT()

## when programme start to run it have to create a python dict in memory with data from filename
def createDictPersonalities(filename):
    """ create a dictionary from
        @input: filename in dictionary format
        @return: a python dictionary
        note: is made exclusively for the file personalities.txt """
    with open(filename, 'r') as f:
        personalities=eval(f.read())
        p = personalities['listPersonalities']
        return p

# ## MAIN FUNCTIONS

def finalPersonalities(text):
    """ match the NamedEntities extracted from the input text 
        with the names in the personalities file.
        @input: text string
        @return: list with referenced persnalities (PERSON) """
    finallist = []
    persons = extractEntities(text)
    for person in persons:
        pessoa= isPersonalitieFamous(person)
        if pessoa!=False and pessoa not in finallist:
            finallist.append(pessoa)
    return finallist


# ## AUXILIAR FUNCTIONS

def isPersonalitieFamous(name, p = createDictPersonalities(filename)):
    """ receives a name and search in personalities SAPO DB if the person
    exists and retrieve the more famous if found more than one 
    @input: name - text string
    @return: person if exists at least one, False otherwise """
    famous = 0
    person = False
    for key in p:
        if name in key:
            if p[key] > famous:
                famous = p[key]
                person = key
    return person

def isPersonalitie(name, p = createDictPersonalities(filename)):
    """ receives a name and search in personalities SAPO DB if a person
    with that name exists.
    @input: name - text string
    @return: person (the first that match the condition), False otherwise """
    for key in p:
        if name in key:
            return key
    return False

def extractEntities(text):
    """ extract NamedEntities (filter only PERSON chunk) and retrieve a list
    @input: text - string - that could be a big text with lot of sentences 
    @return: a list with the Named Entities found (and filtered by PERSON chunk) 
    note: this function uses default NLTK pos_tag and ne_chunk to find Named Entities
    using the text with ascii encoding ignoring special characters, in the end it 
    does a match with original unicode portuguese words to mantain the original chars"""
    returnlist = []
    outputlist = []
    asciitext = text.encode('ascii','ignore') # text to encode ascii
    originaltext = text # original text
    originalwordslist = token.compound_tokenizePT(originaltext, "TB") # original words in unicode
    asciiwordsdict = token.special_tokenizerEN(asciitext)
    asciiwordslist = token.compound_tokenizeEN(asciitext)
    for chunk in nltk.ne_chunk(nltk.pos_tag(asciiwordslist)):
        if hasattr(chunk, 'node') and chunk.node=="PERSON":
            returnlist.append(' '.join(c[0] for c in chunk.leaves()))
    for wordbox in returnlist:
        wordbox = wordbox.split(" ")
        for word in wordbox:
            index = asciiwordsdict[word]
            outputlist.append(originalwordslist[index])
    return outputlist

            

#def main():
    

    
#main()