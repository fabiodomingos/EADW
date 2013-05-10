'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Main Function to invoke all the functions

When a search is performed, the result should include the sentimental on each person
in each returned news item

- other analysis could also been invoked here and creat another functions/py modules

'''
import NewsCollectionAndStorage
import NewsSearch
import SentimentAnalysis
import NLP_PT

# newsFeedName
newsFeedNames = ['dn', 'jn']
newsFeedNamesEnum = enumerate(newsFeedNames)
# FEEDs URLS
DN = "http://feeds.dn.pt/DN-Politica"
JN = "http://feeds.jn.pt/JN-Politica"

token = NLP_PT.tokenizerPT()

## RUN
sentilexfile='SentiLex-PT02/SentiLex-lem-PT02.txt'
sentilexDic = SentimentAnalysis.extractSentilex(sentilexfile)

#interface
while(1):
    print "DATA MINING - INTERFACE"
    print "1 - Populate DB"
    print "2 - Collect new News"
    print "3 - Search in the news"
    
    option = raw_input("Select an option: ")
    
    if option == "1":
        print "Tem ao seu dipor o JN e o DN"
        feed = raw_input("Select your Newspaper: ")
        if feed=="DN":
            feed=DN
            NewsCollectionAndStorage.poppulateIndex(feed)
            NewsSearch.printAll()
            continue
        elif feed=="JN":
            feed=JN
            NewsCollectionAndStorage.poppulateIndex(feed)
            NewsSearch.printAll()
            continue
        else:
            print "Invalid Input: You need to choose JN or DN"
    
    elif option == "2":
        print "Tem ao seu dipor o JN e o DN"
        feed = raw_input("Select your Newspaper: ")
        if feed=="DN":
            feed=DN
            NewsCollectionAndStorage.collectNewNotices(feed)
            NewsSearch.printAll()
            continue
        elif feed=="JN":
            feed=JN
            NewsCollectionAndStorage.collectNewNotices(feed)
            NewsSearch.printAll()
            continue
        else:
            print "Invalid Input: You need to choose JN or DN"
    
    elif option == "3":
        search = raw_input("Find the news with word: ")
        NewsSearch.searchByRelevance(search)
        
        while(1):            
            print "1 - Search the Personalities in the news with your word"
            print "2 - Qualify the News with your word"
            print "0 - Return to Interface"
            
            menuOption= raw_input("Select an option: ")
            
            if menuOption == "1":
                NewsSearch.searchByPersonalitie(search)
                continue
            
            elif menuOption == "2":
                NewsSearch.searchByQualify(search, sentilexDic)
                continue
            
            elif menuOption == "0":
                break
            else: 
                print "Invalid Input: Insert the option Number.\n"
                continue    
    else:
        print "Invalid Input: Insert the option Number.\n"
        continue