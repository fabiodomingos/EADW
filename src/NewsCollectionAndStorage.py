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

# create a new Table with 
def createTable():
    # create a table
    #cursor.execute("""CREATE TABLE newsfeeds
    #                 (newsfeedname text, title text, content text, date text) 
    #              """)
    cursor.execute('''CREATE TABLE news (titulo TEXT, conteudo TEXT, date TEXT)''')


# Insert new New on the table news
def addNew(titulo, conteudo,date):
    cursor.execute('''INSERT INTO news (titulo, conteudo, date)
    VALUES (?,?,?)''',(titulo,conteudo,date))
    
## This function populate a db
## without care about updated time
## just pick up all the news item and put it into the db
def poppulateDb(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    for item in newsFeed.entries:
        titleIn = item.title
        contentIn = item.description
        dateIn = item.published_parsed
        dateFinal = datetime(dateIn[0], dateIn[1], dateIn[2], dateIn[3], dateIn[4],dateIn[5])
        # insert some data
        addNew(titleIn,contentIn,dateFinal)

# function to search if there are new news and collect them
def collectNewItems(newsFeedX):
    cursor.execute('SELECT * FROM news ASC LIMIT 1')
    
    
        
# function to store items in the correspondent table        
def storageItems(*args):
    print "storageNewItems"

 
def main():
    createTable()
    
    poppulateDb(newsFeedJN)
      
    conn.commit()
    
    poppulateDb(newsFeedDN)
    
    conn.commit()
    
    #collectNewItems(newsFeedDN)
    cursor.execute('SELECT * FROM news')
    
    for i in cursor:
        print "\n"
        for j in i:
            print j
    
main()

