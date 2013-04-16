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
from whoosh.index import open_dir   
from whoosh.fields import Schema
from whoosh.fields import DATETIME
from whoosh.fields import TEXT
from whoosh.qparser import QueryParser, OrGroup
import os.path
import re

#TODO: identify news items
#TODO: identify new news items
#TODO: collect and store -> common repository

### newsFeedName
newsFeedNames =['dn','jn']
newsFeedNamesEnum = enumerate(newsFeedNames)

### FEEDs URLS
newsFeedDN = "http://feeds.dn.pt/DN-Politica"
newsFeedJN = "http://feeds.jn.pt/JN-Politica"

conn = sqlite3.connect("teste.db")
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
    ## conteudo pode ser 
    schema = Schema(content=TEXT(stored=True), date=DATETIME, title=TEXT(stored=True))  
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", schema)
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
    index = createIndexWhoosh()
    writer = index.writer()
    for item in newsFeed.entries:
        titleIn = item.title
        contentIn = item.description
        contentOut = remove_html_tags(contentIn)
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        # insert some data in database
        addNew(titleIn,contentOut,dateFinal)
        # whoosh
        writer.add_document(content=contentIn, date=dateFinal, title=titleIn)
    writer.commit()

# SERVE APENAS PARA FAZER TESTES DE METER COISAS NA DB
def populateTeste():
    d=feedparser.parse(newsFeedJN)
    titulo = d['entries'][2]['title']
    conteudo = d['entries'][2]['description']
    contentOut = remove_html_tags(conteudo)
    dateIn = d['entries'][2]['published_parsed']
    dataFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
    addNew(titulo,contentOut,dataFinal)

# Print all db elements    
def getAllDb():
    cursor.execute('SELECT * FROM news ORDER BY date DESC')
    for i in cursor:
        print "\n"
        for j in i:
            print j

def getLastUpdatedDate():
    cursor.execute('SELECT date FROM news ORDER BY date DESC LIMIT 1')
    for i in cursor:
        # Converte o tuplo para string 
        tuploTOstr = "".join(i)
        # Converte a string unicode para datetime
        date=datetime.strptime(tuploTOstr, '%Y-%m-%d %H:%M:%S')
        return date

# Funtion to remove htlm tags of feeds elements
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# function to search if there are new news and collect them
def collectNewItems(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    lastDbDate = getLastUpdatedDate()
    for item in newsFeed.entries:
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        if(dateFinal > lastDbDate):
            titleIn = item.title
            contentIn = item.description
            contentOut = remove_html_tags(contentIn)
            # insert some data
            addNew(titleIn,contentOut,dateFinal)
            
            
def query_func(user_input):
    ix = open_dir("index")
    with ix.searcher() as searcher: 
        query = QueryParser("content", ix.schema, group=OrGroup).parse(u""+user_input) 
        results = searcher.search(query) 
        for r in results:
            print r
    

 
def main():
    #getLinksNews(newsFeedJN)
    
    #createTable()
    
    #populateTeste()
    #conn.commit()
    
    #######
    #poppulateDb(newsFeedJN)
    #conn.commit()
    #poppulateDb(newsFeedDN)
    #conn.commit()

    collectNewItems(newsFeedJN)
    conn.commit
    
    #a=getLastUpdatedDec()
    #remove_html_tags(a)
    
    getAllDb()
    
    #getLastUpdatedDate()
        
    #url = "http://feeds.dn.pt/~r/DN-Politica/~3/JzTprZ3hDqQ/story01.htm"    
    #html = urlopen(url).read()    
    #raw = nltk.clean_html(html)  
    #print(raw)

main()
