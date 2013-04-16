'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

1) pull public news feed
2) identify 
3) collect new news items
4) store them in a common repository for further processing

- Notes:
The news collection should be performed on demand - invoking a function?
and new news items found should be added to the repository.

- Doubts to decide:
Where do we'll store the new items? Which platform/type/file?
Use sqlit3?

'''

### IMPORTS
import feedparser
import sqlite3
from datetime import datetime
from whoosh.index import create_in 
from whoosh.fields import Schema
from whoosh.fields import NUMERIC
from whoosh.fields import TEXT

import nltk   
from urllib import urlopen

#TODO: identify news items
#TODO: identify new news items
#TODO: collect and store -> common repository

### newsFeedName
newsFeedNames =['dn','jn']
newsFeedNamesEnum = enumerate(newsFeedNames)

### FEEDs URLS
newsFeedDN = "http://feeds.dn.pt/DN-Politica"
newsFeedJN = "http://feeds.jn.pt/JN-Politica"

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# create a new Table with titulo, conteudo, data
# this function is just called once
def createTable():
    # create a table
    #cursor.execute("""CREATE TABLE newsfeeds
    #                 (newsfeedname text, title text, content text, date text) 
    #              """)
    cursor.execute('''CREATE TABLE news (titulo TEXT, conteudo TEXT, date TEXT)''')
    
# create a new Index for Whoosh
# @returns: ix - Index Object 
def createIndexWhoosh():
    schema = Schema(id = NUMERIC(stored=True), content=TEXT)  ## TODO: confirmar campo stored : o que faz
    ix = create_in("indexdir", schema)
    return ix
    

# AUX Function
# Insert new 'New' on the table news
def addNew(titulo, conteudo,date):
    cursor.execute('''INSERT INTO news (titulo, conteudo, date)
    VALUES (?,?,?)''',(titulo,conteudo,date))
    
# AUX Function    
# get the link for the whole news (not only the resume)
def getLinksNews(newsFeedX):
    newsLink = feedparser.parse(newsFeedX)
    print newsLink['entries'][0]['link'] 
            
## This function populate a db
## without care about updated time
## just pick up all the news item and put it into the db
## This function is called once - to poppulate the db in the beginning
def poppulateDb(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    for item in newsFeed.entries:
        titleIn = item.title
        contentIn = item.description
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        # insert some data in database
        addNew(titleIn,contentIn,dateFinal)
        # whoosh
        #index = createIndexWhoosh()
        #writer = index.writer()
        #writer.add_document(id=i, content=contentIn)

    
def getAllDb():
    cursor.execute('SELECT * FROM news ORDER BY date DESC')
    for i in cursor:
        print "\n"
        for j in i:
            print j

def getLastUpdatedDate():
    cursor.execute('SELECT date FROM news ORDER BY date DESC LIMIT 1')
    for i in cursor:
        return i
    
# function to search if there are new news and collect them
def collectNewItems(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    for item in newsFeed.entries:
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        # if(dateFinal )
        titleIn = item.title
        contentIn = item.description
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        # insert some data
        addNew(titleIn,contentIn,dateFinal)
    conn.commit()
    

 
def main():
    #getLinksNews(newsFeedJN)
    
    createTable()
    
    #######
    poppulateDb(newsFeedJN)
    conn.commit()
    poppulateDb(newsFeedDN)
    conn.commit()

    getLastUpdatedDate()
        
    #url = "http://feeds.dn.pt/~r/DN-Politica/~3/JzTprZ3hDqQ/story01.htm"    
    #html = urlopen(url).read()    
    #raw = nltk.clean_html(html)  
    #print(raw)
    
    
    
main()

