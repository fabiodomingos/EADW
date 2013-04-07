'''
Created on 2013/04/05

@author: goncalocarito
@authro: fabiodomings

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

#TODO: identify news items
#TODO: identify new news items
#TODO: collect and store -> common repository

### FEEDs URLS
newsFeedDN = "http://feeds.dn.pt/DN-Politica"
newsFeedJN = "http://feeds.jn.pt/JN-Politica"

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create a new Table with 
def createTable(newsFeedName):
    # create a table
    #cursor.execute("""CREATE TABLE newsFeedName
    #                 (title text, content text, release_date text) 
    #              """)
    print ""

## This function populate a db
## without care about updated time
## just pick up all the news item and put it into the db
def poppulateDb(newsFeedX):
    newsFeed = feedparser.parse(newsFeedX)
    for item in newsFeed.entries:
        titleIn = item.title
        contentIn = item.description
        dateIn = item.published
        # insert some data
        #cursor.execute("INSERT INTO dn VALUES (titleIn, contentIn, dateIn)")
        return titleIn, contentIn, dateIn

#titleDb, contentDb, dateDb = poppulateDb(newsFeedDN)

#print titleDb
#print contentDb
#print dateDb

# function to search if there are new news and collect them
def collectNewItems(newsFeedX):
    #TODO
    newsFeed = feedparser.parse(newsFeedX)
    print newsFeed.feed.title
    lastUpdatedFeed = newsFeed.feed.updated
    lastUpdatedSystem = 0

    # update time
    def update():
        lastUpdatedSystem = lastUpdatedFeed
        
    for item in newsFeed.entries:
        print item
        
# function to store items in the correspondent table        
def storageItems(*args):
    print ""

