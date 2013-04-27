'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

1) pull public news feed
2) identify 
3) collect new news items
4) store them in a common repository for further processing

- Notes:
The news collection should be performed on demand
and new news items found should be added to the repository.


'''
# # OPTIONAL TODO
# # Implement the real articles linked by the feed
# # to do that is necessary to explore STORED/JUST INDEXED ITEMS and how it works

# # MORE THAN OPTIONAL TODO
# # Explore whoosh documentation: http://pythonhosted.org/Whoosh/index.html
# # and do awesome things with that


# ## IMPORTS
from datetime import datetime
from whoosh.fields import DATETIME, Schema, TEXT
from whoosh.index import create_in, open_dir
import NewsSearch
import feedparser
import os.path
import re
import sqlite3


# ## INITS

# newsFeedName
newsFeedNames = ['dn', 'jn']
newsFeedNamesEnum = enumerate(newsFeedNames)
# FEEDs URLS
newsFeedDN = "http://feeds.dn.pt/DN-Politica"
newsFeedJN = "http://feeds.jn.pt/JN-Politica"
newsFeedTeste = r'/Users/guntty/git/EADW/src/teste.xml'


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
        contentIn = item.description
        contentFinal = remove_html_tags(contentIn)
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        writer.add_document(content=contentFinal, date=dateFinal, title=titleFinal)
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
            contentIn = item.description
            contentFinal = remove_html_tags(contentIn)
            writer.add_document(content=contentFinal, date=dateFinal, title=titleFinal)
    writer.commit()
    
    
# ## AUXILIAR FUNCTIONS

def getLinksNews(newsFeedX):
    """ NOT USED FOR NOW       
        get the link for the whole news (not only the resume) """
    newsLink = feedparser.parse(newsFeedX)
    print newsLink['entries'][0]['link'] 
    
def remove_html_tags(data):
    """ removes html tags of feeds elements """
    p = re.compile(r'<.*?>')
    return p.sub('', data)
    

 
#def main():
   # poppulateIndex(newsFeedJN)
    #NewsSearch.printAll()
    #collectNewNotices(newsFeedDN)
    #NewsSearch.printAll()

#main()



#===============================================================================
#  SQLITE FUNCTIONS - NOT USED NOW - MAYBE WE WILL HAVE THE OPTION TO CHOOSE
#===============================================================================

# initializing the database
conn = sqlite3.connect("teste.db")
# initializing the cursor
cursor = conn.cursor()

# create a new Table with titulo, conteudo, data
# this function is just called once
def createTable():
    # create a table
    # cursor.execute("""CREATE TABLE newsfeeds
    #                 (newsfeedname text, title text, content text, date text) 
    #              """)
    cursor.execute('''CREATE TABLE news (titulo TEXT, conteudo TEXT, date TEXT)''')
    
# AUX Function
# Insert new 'New' on the table news
def addNew(titulo, conteudo, date):
    cursor.execute('''INSERT INTO news (titulo, conteudo, date)
    VALUES (?,?,?)''', (titulo, conteudo, date))
    
# # This function populate a db
# # without care about updated time
# # just pick up all the news item and put it into the db
# # This function is called once - to poppulate the db in the beginning
def poppulateDb(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    for item in newsFeed.entries:
        titleIn = item.title
        contentIn = item.description
        contentOut = remove_html_tags(contentIn)
        # print contentOut
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        # insert some data in database
        addNew(titleIn, contentOut, dateFinal)
        
# SERVE APENAS PARA FAZER TESTES DE METER COISAS NA DB
def populateTeste():
    d = feedparser.parse(newsFeedJN)
    titulo = d['entries'][2]['title']
    conteudo = d['entries'][2]['description']
    contentOut = remove_html_tags(conteudo)
    dateIn = d['entries'][2]['published_parsed']
    dataFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
    addNew(titulo, contentOut, dataFinal)
    
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
        date = datetime.strptime(tuploTOstr, '%Y-%m-%d %H:%M:%S')
        return date
    
# function to search if there are new news and collect them
def collectNewItemsSqLite(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    lastDbDate = getLastUpdatedDate()
    for item in newsFeed.entries:
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4], dateIn[5])
        if(dateFinal > lastDbDate):
            titleIn = item.title
            contentIn = item.description
            contentOut = remove_html_tags(contentIn)
            # insert some data
            addNew(titleIn, contentOut, dateFinal)
            
