#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

1) pull public news feed
2) identify 
3) collect new news items
4) store them in a common repository for further processing


'''

# ## IMPORTS
from datetime import datetime
from whoosh.fields import DATETIME, Schema, TEXT
from whoosh.index import create_in, open_dir
from bs4 import BeautifulSoup as BS
import NewsSearch
import feedparser
import os.path
#import sqlite3
import requests


# ## INITS

# newsFeedName
newsFeedNames = ['dn', 'jn']
newsFeedNamesEnum = enumerate(newsFeedNames)
# FEEDs URLS
newsFeedDN = "http://feeds.dn.pt/DN-Politica"
newsFeedJN = "http://feeds.jn.pt/JN-Politica"


# ## MAIN FUNCTIONS    

def createIndex():
    """ create a new Whoosh Index with the schema: title, content and date of the news feed
    @returns: the Index object """
    schema = Schema(content=TEXT(stored=True), date=DATETIME(stored=True), title=TEXT(stored=True))
    # verify if the index dir exists in filesystem 
    # if not create a new one after creating the index itself
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", schema)
    return ix

def poppulateIndex(newsFeedX):
    """ insert news in the Index without caring about updated time
        just picking up all the news item from news feed
        this function is intended to called only once time:
        - in the beginning of the execution
        - or - in a real situation - when a new NewsFeed is added to the program
    """
    indexGeral=createIndex()
    newsFeed = feedparser.parse(newsFeedX)
    writer = indexGeral.writer()
    for item in newsFeed.entries:
        titleFinal = item.title
        newsLink = item.link
        new=getAllNew(newsLink)
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        writer.add_document(content=new, date=dateFinal, title=titleFinal)
    writer.commit()
    
    
def collectNewNotices(newsFeedX):
    """ search if there are new News and collect them 
        how? check if the news in the feed is already in the Index
        comparing it dates with the last stored date"""
    indexGeral=open_dir("index")
    newsFeed = feedparser.parse(newsFeedX)
    writer = indexGeral.writer()
    # this function is defined in NewsSearch module and retrieve the last date insert in index
    lastDate = NewsSearch.getLastDate()
    for item in newsFeed.entries:
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        # only adds a item if it's more recent that the ones stored in the index
        if(dateFinal > lastDate):
            titleFinal = item.title
            newsLink = item.link
            new=getAllNew(newsLink)
            # COLOCAR UM ID PARA NOTICIA
            writer.add_document(content=new, date=dateFinal, title=titleFinal)
    writer.commit()
    
    
# ## AUXILIAR FUNCTIONS
    
# Agarra no link do feed e vai buscar toda a noticia 
def getAllNew(link):
    html = requests.get(link).text
    soup = BS(html)
    new='\n'.join([k.text for k in soup.find(id='Article').find_all('p')])
    return new

#def main():

    #poppulateIndex(newsFeedJN)
    #NewsSearch.printAll()
    #collectNewNotices(newsFeedDN)
    #NewsSearch.printAll()

#main()



#===============================================================================
#  SQLITE FUNCTIONS - NOT USED 
#===============================================================================

# initializing the database
#conn = sqlite3.connect("jn.db")
# initializing the cursor
#cursor = conn.cursor()

# create a new Table with titulo, conteudo, data
# this function is just called once
#def createTable():
    # create a table
    # cursor.execute("""CREATE TABLE newsfeeds
    #                 (newsfeedname text, title text, content text, date text) 
    #              """)
#    cursor.execute('''CREATE TABLE news (titulo TEXT, conteudo TEXT, date TEXT)''')
    
# AUX Function
# Insert new 'New' on the table news
#def addNew(titulo, conteudo, date):
#    cursor.execute('''INSERT INTO news (titulo, conteudo, date)
#    VALUES (?,?,?)''', (titulo, conteudo, date))
    
# # This function populate a db
# # without care about updated time
# # just pick up all the news item and put it into the db
# # This function is called once - to poppulate the db in the beginning
#def poppulateDb(newsFeedX):
#    newsFeed = feedparser.parse(newsFeedX)
#    for item in newsFeed.entries:
#        titleIn = item.title
#       newsLink = item.link
#        new=getAllNew(newsLink)
        # print contentOut
#        dateIn = item.published_parsed
#       dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        # insert some data in database
#       addNew(titleIn, new, dateFinal)
        
# SERVE APENAS PARA FAZER TESTES DE METER COISAS NA DB
#def populateTeste():
    #d = feedparser.parse(newsFeedJN)
    #titulo = d['entries'][2]['title']
    #conteudo = d['entries'][2]['description']
    #contentOut = remove_html_tags(conteudo)
    #dateIn = d['entries'][2]['published_parsed']
    #dataFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
    #addNew(titulo, contentOut, dataFinal)
    
# Print all db elements    
#def getAllDb():
#    cursor.execute('SELECT * FROM news ORDER BY date DESC')
#    for i in cursor:
#        print "\n"
#        for j in i:
#            print j
#            
#def getLastUpdatedDate():
#    cursor.execute('SELECT date FROM news ORDER BY date DESC LIMIT 1')
#    for i in cursor:
#        # Converte o tuplo para string 
#       tuploTOstr = "".join(i)
#      # Converte a string unicode para datetime
#       date = datetime.strptime(tuploTOstr, '%Y-%m-%d %H:%M:%S')
#       return date
#   
# function to search if there are new news and collect them
#def collectNewItemsSqLite(newsFeedX):
#   newsFeed = feedparser.parse(newsFeedX)
#  lastDbDate = getLastUpdatedDate()
#  for item in newsFeed.entries:
#      dateIn = item.published_parsed
#      dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
#     if(dateFinal > lastDbDate):
#         titleIn = item.title
#            newsLink = item.link
#            new=getAllNew(newsLink)
            # insert some data
#            addNew(titleIn, new, dateFinal)

#def main():
#    createTable()
#    poppulateDb(newsFeedDN)
#    getAllDb()

#main()
                
