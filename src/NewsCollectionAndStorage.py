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

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create a new Table with 
def createTable():
    # create a table
    cursor.execute("""CREATE TABLE newsfeeds
                     (newsfeedname text, title text, content text, date text) 
                  """)

#createTable()

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
        #cursor.execute("INSERT INTO dn VALUES (titleIn, contentIn, dateFinal)")
        return titleIn, contentIn, dateFinal

titleDb, contentDb, dateFinalDb = poppulateDb(newsFeedDN)

print titleDb
print contentDb
print dateFinalDb

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

