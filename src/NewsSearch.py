#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Text searches over the news repository.
Input: set of keyword
Output: list of news ranked by relevance (with e.g BM25)

- labs esta feito

'''
## OPTIONAL TODO
## Various types of search like: AND/OR, PHRASE/WORD
## Highlight the results


# IMPORTS
from whoosh.qparser import QueryParser, OrGroup
from whoosh.index import open_dir  
from whoosh.qparser.dateparse import DateParserPlugin
import ExtractNamedEntities
import SentimentAnalysis
import NLP_PT

Sentilex='SentiLex-PT02/SentiLex-lem-PT02.txt'

token = NLP_PT.tokenizerPT()

# ## MAIN FUNCTIONS

# SEARCH    
# function that receives a query and returns a list with news that match
# the search, sorted by BM25
def searchByRelevance(queries):
    """ receives a query
        @returns items resulted by the query search, sorted by BM25
        THIS FUNCTION IS PRINTING IN THE SCREEN NOW"""
    ix = open_dir("index")
    with ix.searcher() as searcher: 
        query = QueryParser("content", ix.schema, group=OrGroup).parse(u""+queries) 
        results = searcher.search(query)
        printResults(results)

def searchByPersonalitie(queries):
    """ receives a query
        @returns items resulted by the query search, sorted by BM25
        THIS FUNCTION IS PRINTING IN THE SCREEN NOW"""
    ix = open_dir("index")
    with ix.searcher() as searcher: 
        query = QueryParser("content", ix.schema, group=OrGroup).parse(u""+queries) 
        results = searcher.search(query)
        printPersons(results)

def searchByQualify(queries, sentilex):
    """ receives a query
        @returns items resulted by the query search, sorted by BM25
        THIS FUNCTION IS PRINTING IN THE SCREEN NOW"""
    ix = open_dir("index")
    with ix.searcher() as searcher: 
        query = QueryParser("content", ix.schema, group=OrGroup).parse(u""+queries) 
        results = searcher.search(query)
        printQualify(results, sentilex)
        
## TODO: search with personalities
        

# ## AUXILIAR FUNCTIONS

def printAll():
    """ dump. print all the items in the Index """
    ix = open_dir('index')
    with ix.searcher() as searcher:
        print "========== PRINTING ALL NEWS ============"
        for doc in searcher.documents():
            print "================ New =============="
            print ">>TITLE"
            print doc['title']
            print ">>CONTENT"
            print doc['content']
            print ">>DATE"
            print doc['date']

def printResults(results):
    """ dump. print all items in a result Object """
    print "========== PRINTING ALL RESULTS ========"
    for r in results:
        print "================ New =============="
        print ">>TITLE"
        print r['title']
        print ">>CONTENT"
        print r['content']
        print ">>DATE"
        print r['date']

def printPersons(results):
    """ dump. print all items in a result Object """
    print "========== PRINTING ALL PERSONS ========"
    for r in results:
        print "================ News =============="
        print ">>TITLE"
        print r['title']
        print ">>CONTENT"
        text=r['content']
        print text
        print ">>PERSONS"
        person=ExtractNamedEntities.finalPersonalities(text)
        print person
        
def printQualify(results, extractsentilex):
    """ dump. print all items in a result Object """
    print "========== PRINTING ALL PERSONS ========"
    for r in results:
        print "================ News =============="
        print ">>TITLE"
        print r['title']
        print ">>CONTENT"
        text=r['content']
        print text
        print ">>QUALIFY"
        qualify=SentimentAnalysis.qualifyNew(token.filter(text), extractsentilex)
        print qualify
            
def getLastNotice():
    """ @returns the last added notice to the Index """
    ix = open_dir("index")
    with ix.searcher() as searcher: 
        qp = QueryParser("content", ix.schema, group=OrGroup)
        qp.add_plugin(DateParserPlugin())
        query = qp.parse(u"date:'[18000101 to today]") 
        results = searcher.search(query, limit=1) 
        return results.fields(0)

def getLastDate():
    """ @returns the last date (date of the last added notice """
    hit = getLastNotice()
    dateFinal = hit['date']
    return dateFinal

#printAll()
#search("país")

