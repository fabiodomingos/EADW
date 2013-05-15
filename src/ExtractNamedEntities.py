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
import json


# ## INITIALIZATIONS

# instance of NLP_PT
token = NLP_PT.tokenizerPT()

# import politicinas file to a dict
politicians = json.load(open("politicians.txt"))

# ## MAIN FUNCTIONS

def finalPersonalities(text, politicians_local):
    """ match the NamedEntities extracted from the input text 
        with the names in the personalities file.
        @input: text string
        @return: list with referenced persnalities (PERSON) """
    finallist = []
    persons = extractEntities(text)
    for person in persons:
        pessoa=isPersonalitieFamous(person)
        if pessoa!=False and pessoa not in finallist:
            if pessoa not in politicians_local:
                politicians_local.update({pessoa: (1, politicians[pessoa][1])})
            else:
                politicians_local.update({pessoa: (politicians_local[pessoa][0] + 1, politicians[pessoa][1])})
    return politicians_local;

def retrievePersonalities(text):
    finallist = []
    persons = extractEntities(text)
    for person in persons:
        pessoa=isPersonalitieFamous(person)
        if pessoa!=False and pessoa not in finallist:
            finallist.append(pessoa)
    return finallist;

def mostPopularPolitician(dicti):
    return max(dicti.iterkeys(), key=(lambda key: dicti[key][0]))

def mostPopularParty(dicti):
    parties = {'PS': 0 , 'PSD' : 0, 'BE':0, 'CDS-PP':0, 'PCP':0, 'PRD':0, 'ASDI':0,'MDPCDE':0,'PEV':0,'UEDS':0,'CDS':0,'UDP':0,'DR':0,'PSN':0,'PPM':0,'ID':0}
    for key in dicti:    
        if dicti[key][1] == "PS":
            parties["PS"] = parties["PS"] + dicti[key][0]
        elif dicti[key][1] == "PSD":
            parties["PSD"] = parties["PSD"] + dicti[key][0]
        elif dicti[key][1] == "BE":
            parties["BE"] = parties["BE"] + dicti[key][0]
        elif dicti[key][1] == "CDS-PP":
            parties["CDS-PP"] = parties["CDS-PP"] + dicti[key][0]
        elif dicti[key][1] == "PCP":
            parties["PCP"] = parties["PCP"] + dicti[key][0]
        elif dicti[key][1] == "PRD":
            parties["PRD"] = parties["PRD"] + dicti[key][0]
        elif dicti[key][1] == "ASDI":
            parties["ASDI"] = parties["ASDI"] + dicti[key][0]
        elif dicti[key][1] == "MDPCDE":
            parties["MDPCDE"] = parties["MDPCDE"] + dicti[key][0]
        elif dicti[key][1] == "PEV":
            parties["PEV"] = parties["PEV"] + dicti[key][0]
        elif dicti[key][1] == "UEDS":
            parties["UEDS"] = parties["UEDS"] + dicti[key][0]
        elif dicti[key][1] == "CDS":
            parties["CDS"] = parties["CDS"] + dicti[key][0]
        elif dicti[key][1] == "UDP":
            parties["UDP"] = parties["UDP"] + dicti[key][0]
        elif dicti[key][1] == "DR":
            parties["DR"] = parties["DR"] + dicti[key][0]
        elif dicti[key][1] == "PSN":
            parties["PSN"] = parties["PSN"] + dicti[key][0]
        elif dicti[key][1] == "PPM":
            parties["PPM"] = parties["PPM"] + dicti[key][0]
        elif dicti[key][1] == "ID":
            parties["ID"] = parties["ID"] + dicti[key][0]
    return max(parties.iterkeys(), key=(lambda key: parties[key]))

# ## AUXILIAR FUNCTIONS

def isPersonalitieFamous(name, p = politicians):
    """ receives a name and search in personalities SAPO DB if the person
    exists and retrieve the more famous if found more than one 
    @input: name - text string
    @return: person if exists at least one, False otherwise """
    famous = -1
    person = False
    for key in p:
        # se o nome é uma só palavra evita procurar dentro de outro nome de uma so palavra
        if len(name.split(" ")) == 1:
            for word in key.split(" "):
                if name == word:
                    if p[key][0] > famous:
                        famous = p[key][0]
                        if famous < 10:
                            person = False
                        else:
                            person = key
        else:
            if name in key:
                if p[key][0] > famous:
                    famous = p[key][0]
                    person = key
    return person

def isPersonalitie(name, p = politicians):
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
    asciitext = removeNonAscii(text)
    originaltext = text # original text
    originalwordsdict = token.special_tokenizerPT(originaltext)
    asciiwordsdict = token.special_tokenizerEN(asciitext)
    asciiwordslist = token.compound_tokenizeEN(asciitext)
    for chunk in nltk.ne_chunk(nltk.pos_tag(asciiwordslist), binary=False):
        if hasattr(chunk, 'node') and chunk.node=="PERSON":
            returnlist.append(' '.join(originalwordsdict[asciiwordsdict[c[0]]] for c in chunk.leaves()))
    return returnlist

def removeNonAscii(s): 
    return "".join([x if ord(x) < 128 else 'a' for x in s])

            

#def main():
    

    
#main()