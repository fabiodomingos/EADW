'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Text searches over the news repository.
Input: set of keyword
Output: list of news ranked by relevance (with e.g BM25)

- labs est‡ feito

'''

# function that creates a whoosh index with all the news
def createIndex():
    print "createindex"
    
# function that receives a query and returns a list with news that match
# the search, sorted by BM25
def search(queries):
    print "search"