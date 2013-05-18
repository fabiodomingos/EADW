#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Text searches over the news repository.
Input: set of keyword
Output: list of news ranked by relevance (with e.g BM25)


'''

# IMPORTS
from whoosh.qparser import QueryParser, OrGroup
from whoosh.index import open_dir  
from whoosh.qparser.dateparse import DateParserPlugin
import ExtractNamedEntities
import SentimentAnalysis
import NLP_PT
import json
import os


## INITIALIZATIONS

# token por portuguese language
token = NLP_PT.tokenizerPT()

# temporary and history files
filepartiesH = "parties_history.txt"
filequeries = "queries.txt"
filepoliticsH = "politicians_history.txt"
filequeriesH = "queries_history.txt"
fileparties = "parties.txt"


# ## MAIN FUNCTIONS

# SEARCH    
# function that receives a query and returns a list with news that match
# the search, sorted by BM25
def search(queries):
    """ receives a query
    @returns items resulted by the query search, sorted by BM25 printed """
    politic_local = {}
    person = {}
    if os.path.exists(filequeries):
        listqueries = json.load(open(filequeries))
    else:
        listqueries = []
    listqueries.append(queries)
    json.dump(listqueries, open(filequeries, 'w'))
    
    if os.path.exists(fileparties):
        listparties = json.load(open(fileparties))
    else:
        listparties = []
        
    ix = open_dir("index")
    query = QueryParser("content", ix.schema, group=OrGroup).parse(u"" + queries) 
    results = ix.searcher().search(query, limit=None)
    if len(results) == 0:
        print "Your search had no results."
        return results, {}, 0
    for i, r in enumerate(results):
        person = ExtractNamedEntities.finalPersonalities(r['content'], politic_local)
        for p in person:
            listparties.append(person[p][1])
    print "Your search resulted in - " + str(i+1) + " - news.\n"
    json.dump(list(set(listparties)), open('parties.txt', 'w'))
    json.dump(person, open('politicians_local.txt', 'w'))
    return results, person, i, 
        
        
# ## AUXILIAR PRINT FUNCTIONS

# FOR SEARCHES

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
        print ">>SEARCH HIGHLIGHT"
        print r.highlights('content')
        print ">>DATE"
        print r['date']


def printPersons(results):
    """ dump. print all items in a result Object
    @ return: printing with title and politicians in the news
    invoking ExtractedNamedEntities module """
    print "========== PRINTING ALL PERSONS ========"
    for r in results:
        print "================ News =============="
        print ">>TITLE"
        print r['title']
        print ">>PERSONS"
        persons = ExtractNamedEntities.retrievePersonalities(r['content'], 0)
        for p in persons:
            print p
        
def printMostPopularPolitician():
    """ print to the screen the most popular politician in a search """
    print "========== MOST POPULAR POLITICIAN ========="
    filen = "politicians_local.txt"
    if not os.path.exists(filen):
        print "You have to do a search first."
    else:
        politicians = json.load(open(filen))
        print ExtractNamedEntities.mostPopularPolitician(politicians)

def printMostPopularParty():
    """ print in the screen the most popular party (related to politicians) in a search """
    print "========== MOST POPULAR PARTY =========="
    filen = "politicians_local.txt"
    if not os.path.exists(filen):
        print "You have to do a search first."
    else:
        politicians = json.load(open(filen))
        print ExtractNamedEntities.mostPopularParty(politicians)


# FOR HISTORY

def printQueriesHistory(local=False):
    """ print a list of searched queries
    local=False is all time history
    local=True is only current session """
    # # caso iremos imprimir historico
    merge = []
    if local == False:
        if os.path.exists(filequeriesH):
            print "========= QUERIES HISTORY ======"
            histqueries = json.load(open(filequeriesH))
            if os.path.exists(filequeries):
                tempqueries = json.load(open(filequeries))
                merge = histqueries + tempqueries
                histqueries = merge
            for q in histqueries:
                print q 
        else:
            return True
    # # caso iremos imprimir sessao local (local = True)
    else:
        if os.path.exists(filequeries):
            print "========= QUERIES HISTORY ======"
            localqueries = json.load(open(filequeries))
            for l in localqueries:
                print l
        else:
            return True


def printPersonHistory(local=False):
    """ print list of persons that appeared in news
    local=False is all time history
    local=True is only for the current search """
    fileG = "politicians_global.txt"
    fileH = "politicians_history.txt"
    # # caso iremos imprimir historico
    if local == False:
        if os.path.exists(fileH):
            print "========= POLITICIANS HISTORY ======"
            hist = json.load(open(fileH))
            if os.path.exists(fileG):
                locald = json.load(open(fileG))
                ##
                for key in locald.keys():
                    if key in hist.keys():
                        hist[key][0] = hist[key][0] + locald[key][0]
                    else:
                        hist.update({key:(locald[key][0], locald[key][1])})
                ##
            for person in hist.keys():
                print person
        else:
            return True
    # # caso iremos imprimir sessao local (local = True)
    else:
        if os.path.exists(fileG):
            print "========= POLITICIANS HISTORY ======"
            locald = json.load(open(fileG))
            for l in locald.keys():
                print l
        else:
            return True
        
def printPartyHistory(local=False):
    """ print a list of Political Parties retrieved in searches
    local = False is for all time searches
    local = True is only for the current search """
    merge = []
    # # caso iremos imprimir historico
    if local == False:
        if os.path.exists(filepartiesH):
            print "========= PARTIES HISTORY ======"
            hist = json.load(open(filepartiesH))
            if os.path.exists(fileparties):
                temp = json.load(open(fileparties))
                merge = hist + temp
                merge = list(set(merge))
                hist = merge
            for q in hist:
                print q 
        else:
            return True
    # # caso iremos imprimir sessao local (local = True)
    else:
        if os.path.exists(fileparties):
            print "========= PARTIES HISTORY ======"
            locald = json.load(open(fileparties))
            for l in locald:
                print l
        else:
            return True
        
def printMostPopularPoliticianHistory(local=False):
    """ print the most popular politician in a history
    local = False history is all the searches done
    local = True is only the current session """
    fileG = "politicians_global.txt"
    # # caso iremos imprimir historico
    if local == False:
        if os.path.exists(filepoliticsH):
            print "========== MOST POPULAR POLITICIAN HISTORY ========="
            hist = json.load(open(filepoliticsH))
            if os.path.exists(fileG):
                locald = json.load(open(fileG))
                ##
                for key in locald.keys():
                    if key in hist.keys():
                        hist[key][0] = hist[key][0] + locald[key][0]
                    else:
                        hist.update({key:(locald[key][0], locald[key][1])})
                ##
            print ExtractNamedEntities.mostPopularPolitician(hist)
        else:
            return True
    # # caso iremos imprimir sessao local (local = True)
    else:
        if os.path.exists(fileG):
            print "========== MOST POPULAR POLITICIAN HISTORY ========="
            locald = json.load(open(fileG))
            print ExtractNamedEntities.mostPopularPolitician(locald)
        else:
            return True

def printMostPopularPartyHistory(local=False):
    """ print the most popular political party in a history
    local = False history is all the searches done
    local = True is only the current session """
    fileG = "politicians_global.txt"
    # # caso iremos imprimir historico
    if local == False:
        if os.path.exists(filepoliticsH):
            print "========== MOST POPULAR PARTY HISTORY ========="
            hist = json.load(open(filepoliticsH))
            if os.path.exists(fileG):
                locald = json.load(open(fileG))
                for key in locald.keys():
                    if key in hist.keys():
                        hist[key][0] = hist[key][0] + locald[key][0]
                    else:
                        hist.update({key:(locald[key][0], locald[key][1])})
            print ExtractNamedEntities.mostPopularParty(hist)
        else:
            return True
    # # caso iremos imprimir sessao local (local = True)
    else:
        if os.path.exists(fileG):
            print "========== MOST POPULAR PARTY HISTORY ========="
            locald = json.load(open(fileG))
            print ExtractNamedEntities.mostPopularParty(locald)
        else:
            return True
        
## # AUXILIAR SAVE FUNCTIONS        
        
def savePolitics():
    """ save the content of politicians found in a search to a temporary file
    where could have more or not politicians found in another searches did in the current session """
    filen = "politicians_local.txt"
    fileg = "politicians_global.txt"
    if not os.path.exists(filen):
        pass
    else:
        politiciansN = json.load(open(filen))
        if not os.path.exists(fileg):
            politiciansG = politiciansN
        else:
            politiciansG = json.load(open(fileg))
            for k in politiciansN.keys():
                if k in politiciansG.keys():
                    politiciansG[k][0] = politiciansG[k][0] + politiciansN[k][0]
                else:
                    politiciansG.update({k:(politiciansN[k][0], politiciansN[k][1])})
        json.dump(politiciansG, open(fileg, 'w'))

def savePoliticsHistory():
    """ save politicians found to all time history persistent file """
    fileg = "politicians_global.txt"
    fileh = filepoliticsH
    if not os.path.exists(fileg):
        pass
    else:
        politiciansG = json.load(open(fileg))
        if not os.path.exists(fileh):
            politiciansH = politiciansG
        else:
            politiciansH = json.load(open(fileh))
            for k in politiciansG.keys():
                if k in politiciansH.keys():
                    politiciansH[k][0] = politiciansH[k][0] + politiciansG[k][0]
                else:
                    politiciansH.update({k:(politiciansG[k][0], politiciansG[k][1])})
        print politiciansH            
        json.dump(politiciansH, open(fileh, 'w'))
    
def saveQueriesHistory():
    """ save queries searched to persistent file that could be all time history until deleted """
    if not os.path.exists(filequeries):
        pass
    else:
        tempqueries = json.load(open(filequeries))
        print tempqueries
        if os.path.exists(filequeriesH):
            queriesH = json.load(open(filequeriesH))
            merge = queriesH + tempqueries
            tempqueries = merge
            print tempqueries
        json.dump(tempqueries, open(filequeriesH, 'w'))


def savePartiesHistory():
    """ save all parties retrieved from search to history , persistent file that could be or not deleted in another chance """
    if not os.path.exists(fileparties):
        pass
    else:
        tempparties = json.load(open(fileparties))
        print tempparties
        if os.path.exists(filepartiesH):
            partiesH = json.load(open(filepartiesH))
            merge = partiesH + tempparties
            tempparties = list(set(merge))
            print tempparties
        json.dump(tempparties, open(filepartiesH, 'w'))
    
    
def clearHistory(local=False):
    """ clear all the history saved in various sessions """
    returned = False
    if os.path.exists(filequeries) and local == True:
        deleteFile(fileparties)
        deleteFile(filequeries)
        deleteFile("politicians_local.txt")
        deleteFile("politicians_global.txt")
        returned = True
    elif os.path.exists(filequeriesH) and local == False:
        deleteFile(filequeriesH)
        deleteFile(filepartiesH)
        deleteFile(filepoliticsH)
        # # delete also temporary files
        deleteFile(fileparties)
        deleteFile(filequeries)
        deleteFile("politicians_local.txt")
        deleteFile("politicians_global.txt")
    else:
        returned = False
    return returned
    
def deleteFile(myfile):
    """ delete a file 
    @input filename """
    if os.path.isfile(myfile):
        os.remove(myfile)
        


        
def printQualify(results, extractsentilex):
    """ dump. print all items in a result Object """
    print "========== PRINTING ALL PERSONS ========"
    for r in results:
        print "================ News =============="
        print ">>TITLE"
        print r['title']
        text = r['content']
        print ">>QUALIFY"
        SentimentAnalysis.qualifyNew(token.filterStopsSet(text), extractsentilex)
            
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

def printQualifyPolticians(results, sentilex):
    print "========== PRINTING ALL PERSONS ========"
    for r in results:
        print "================ News =============="
        print ">>TITLE"
        print r['title']
        text = r['content']
        print ">>QUALIFY"
        SentimentAnalysis.personSentimenti(SentimentAnalysis.createPOSdict(text), sentilex)
