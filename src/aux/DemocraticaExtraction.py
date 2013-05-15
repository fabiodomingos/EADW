#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
DemocraticaExtraction is a module where is made the extraction of http://demo.cratica.org/deputados/ website
and the match with SAPO personalities.

ADD new politicians to extra dictionary and run this module to obtain a file with the final dict in format - name : [popularity, party]

'''

from bs4 import BeautifulSoup as BS
import requests
import json
link = "http://demo.cratica.org/deputados/?legislature=all&party=all&constituency=all"

filename="personalities.txt"

## Add here the politcians that you want to add to the list
extra = {
   u'Marcelo Rebelo de Sousa': "PSD",
   u'Vitor Gaspar': "PSD",
   u'Miguel Poiares Maduro' : 'PSD',
   u'Álvaro Santos Pereira' : 'PSD',
   u'Paulo Macedo' : 'PSD',
   u'Nuno Crato' : ' ',
   u'Mário Soares' : 'PS',
   u'João Assunção Ribeiro' : 'PS',
   u'Luís Marques Mendes' : 'PSD',
   u'Aníbal Cavaco Silva' : 'PSD',
   u'Alfredo Nobre da Costa' : ' ',
   u"Maria de Lourdes Pintassilgo" : 'PS',
   u'João Cordeiro' : 'PS' 
}


def politiciansExtraction(link):
    party = ""
    politicians = {}
    html = requests.get(link).text
    soup = BS(html)
    span = soup.findAll('span')
    for i, sp in enumerate(span):
        if i % 2 == 0:
            party = sp.text
        else:
            politicians.update({sp.text : party})
    return politicians

def addNewPoliticians(extra, original):
    original.update(extra)
    
def retrievePoliticians():
    link = "http://demo.cratica.org/deputados/?legislature=all&party=all&constituency=all"
    pol = politiciansExtraction(link)
    addNewPoliticians(extra, pol)
    return pol

    
def createDictPersonalities(filename):
    """ create a dictionary from
        @input: filename in dictionary format
        @return: a python dictionary
        note: is made exclusively for the file personalities.txt """
    with open(filename, 'r') as f:
        personalities=eval(f.read())
        p = personalities['listPersonalities']
        return p
    
def toUnicodeDict(dicti):
    output = {}
    for a in dicti:
        output.update({a.decode('UTF-8'): dicti[a]})
    return output

def retrieveFinal():
    demo = retrievePoliticians()
    pers = toUnicodeDict(createDictPersonalities(filename))
    final = {}
    
    for d in demo.keys():
        if d in pers:
            final.update({d:(pers[d], demo[d])})
        else:
            final.update({d:(0, demo[d])})
    return final

final = retrieveFinal()
json.dump(final, open('politicians.txt', 'w'))
        
        