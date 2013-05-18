#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Main Function to invoke all the functions

When a search is performed, the result should include the sentimental on each person
in each returned news item

- other analysis could also been invoked here and creat another functions/py modules

'''
import NewsSearch
import NLP_PT
import os
import NewsCollectionAndStorage
import json


# FEEDs URLS
DN = "http://feeds.dn.pt/DN-Politica"
JN = "http://feeds.jn.pt/JN-Politica"

token = NLP_PT.tokenizerPT()

## RUN

sentilexDic = json.load(open("sentilex.txt"))



while(1):
    print 'INTERFACE - POLITICAL SEARCH'
    print '1 - Collection and Storage'
    print '2 - New Search'
    print '3 - History'
    print '0 - Exit'

    option = raw_input("Select an option: ")
    
    if option == "1":
        while (1):
            print '\n'
            print "COLLECTION AND STORAGE MENU"
            print "1 - Collect new News"
            print "2 - Clean Database and Collect News"
            print "0 - Return to INTERFACE"
            
            menuoption = raw_input("Select an option: ")
            
            if menuoption == "1":
                print "Collecting..."
                NewsCollectionAndStorage.collectNewNotices(JN)
                NewsCollectionAndStorage.collectNewNotices(DN)
                print "News Collected"
                
            elif menuoption == "2":
                opt = raw_input("You will lost some of your old saved content. Are you sure? (y/n) ")
                if opt == "y" or opt == "Y":
                    print "Cleaning..."
                    NewsCollectionAndStorage.poppulateIndex(JN)
                    print "Collecting..."
                    NewsCollectionAndStorage.poppulateIndex(DN)
                    print "Database cleaned and News Collected"
                elif opt == "n" or opt == "N":
                    pass
                else:
                    print "Invalid Input: Insert y or n.\n"
                    continue
            
            elif menuoption =="0":
                break
            
            else:
                print "Invalid Input: Insert the option Number.\n"
                continue
                    

    # OPCAO POR UMA NOVA PESQUISA
    elif option == "2":
        
        # USER DA UMA PALAVRA PARA PESQUISA
        search = raw_input("Insert a word to search: ")
        print "Searching..."
        results, person, i = NewsSearch.search(u""+search)
        
        # MENU SEARCH
        while (1):
            print '\n'
            print "SEARCH MENU"
            print "1 - View News"
            print "2 - View Politicians (by News Title)"
            print "3 - View Politicians (search resume)"
            print "4 - Most Popular Politician"
            print "5 - Most Popular Political Party"
            print "6 - Qualify News"
            print "7 - Qualify Politicians"
            print "0 - Return to INTERFACE"

            menuoption = raw_input("Select an option: ")

            # OPCAO DE VER NOTICIAS DA PESQUISA
            if menuoption == "1":
                NewsSearch.printResults(results)
                print "Query: " + search
                print "In: " + str(i+1) + " news"
                continue

            # OPCAO DE PESQUISAR PESSOAS POR NOTICIA
            elif menuoption == "2":
                NewsSearch.printPersons(results)
                print "Query: " + search
                print "In: " + str(i+1) + " news"
                continue
            
            # OPCAO DE PESQUISAR PESSOAS RESUMO
            elif menuoption == "3":
                for p in person:
                    print p
                continue

            # OPCAO DE PESSOA MAIS INFLUENTE
            elif menuoption == "4":
                NewsSearch.printMostPopularPolitician()
                continue

            # OPCAO DE PARTIDO MAIS INFLUENTE
            elif menuoption == "5":
                NewsSearch.printMostPopularParty()
                continue
            
            # OPCAO DE CLASSIFICAR NOTICIA
            elif menuoption == "6":
                NewsSearch.printQualify(results, sentilexDic)
                continue
            
            # OPCAO DE CLASSIFICAR NOTICIA
            elif menuoption == "7":
                NewsSearch.printQualifyPolticians(results, sentilexDic)
                continue

            # OPCAO DE SAIR
            elif menuoption == "0":
                NewsSearch.savePolitics()
                break

            # OPCAO INVALIDA
            else:
                print "Invalid Input: Insert the option Number.\n"
                continue

    # OPCAO POR VER O HISTORICO
    elif option == "3":
        while (1):
            print '\n'
            print "History MENU"
            print "1 - View 'All Time' History"
            print "2 - View 'This Session' History"
            print "3 - Clear 'All Time' History"
            print "4 - Clear 'This Session' History"
            print "0 - Return to INTERFACE" 
            menuoption = raw_input("Select an option: ")
        
            if menuoption == "1":
                print "=== 'ALL TIME' HISTORY ==="
                if (NewsSearch.printQueriesHistory() == True):
                    print "No data found."
                else:
                    NewsSearch.printPersonHistory()
                    NewsSearch.printPartyHistory()
                    NewsSearch.printMostPopularPoliticianHistory()

            
            elif menuoption == "2":
                print "=== 'THIS SESSION' HISTORY ==="
                if (NewsSearch.printQueriesHistory(local = True) == True):
                    print "No data found."
                else:
                    NewsSearch.printPersonHistory(local = True)
                    NewsSearch.printPartyHistory(local = True)
                    NewsSearch.printMostPopularPoliticianHistory(local = True)
                    NewsSearch.printMostPopularPartyHistory(local = True)
        
            elif menuoption == "3":
                response = raw_input("""This action is going to delete permanently your 'all time' search history. 
Are you sure? (y/n) """)
                if response == "y" or response == "Y":
                    opt = NewsSearch.clearHistory()
                    if opt == True:
                        print "History cleared."
                    else:
                        print "Nothing to clear."
                elif response == "n" or response == "N":
                    pass
                else:
                    print "Invalid Input: Insert y or n.\n"
                    continue
            
            elif menuoption == "4":
                response = raw_input("""This action is going to delete permanently your 'this session' search history. 
Are you sure? (y/n) """)
                if response == "y" or response == "Y":
                    opt = NewsSearch.clearHistory(local = True)
                    if opt == True:
                        print "History cleared."
                    else:
                        print "Nothing to clear."
                elif response == "n" or response == "N":
                    pass
                else:
                    print "Invalid Input: Insert y or n.\n"
                    continue
                    
        
            elif menuoption == "0":
                break
        
            else:
                print "Invalid Input: Insert the option Number.\n"
                continue

    # OPCAO SAIR 
    elif option == "0":
        if os.path.exists("queries.txt") == True:
            option = raw_input("Do you want to save history? (y/n) ")
            if option == "y" or option == "Y":
                print "Saving...\n"
                ## save queries list for history
                NewsSearch.saveQueriesHistory()
                ## save partis list for history
                NewsSearch.savePartiesHistory()
                ## save politicians history
                NewsSearch.savePoliticsHistory()
            elif option == 'n' or option == 'N':
                pass
            else:
                print "Invalid Input: Insert y or n.\n"
                continue
            ## delete temporary files    
            NewsSearch.deleteFile("politicians_local.txt")
            NewsSearch.deleteFile("politicians_global.txt")
            NewsSearch.deleteFile('queries.txt')
            NewsSearch.deleteFile("parties.txt")
        print "Thank you!"
        break

    # OPCAO INVALIDA 
    else:
        print "Invalid Input: Insert the option Number.\n"
        continue

            