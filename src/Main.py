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

NewsCollectionAndStorage.collectNewNotices(JN)
NewsCollectionAndStorage.collectNewNotices(DN)

while(1):
    print 'INTERFACE - DATA MINING POLITICS SEARCH'
    print '1 - New Search'
    print '2 - History'
    print '0 - Exit'

    option = raw_input("Select an option: ")

    # OPCAO POR UMA NOVA PESQUISA
    if option == "1":
        
        # USER DA UMA PALAVRA PARA PESQUISA
        search = raw_input("Insert a word for search: ")
        #NewsSearch.search(search)
        
        # MENU SEARCH
        while (1):
            print '\n'
            print "SEARCH MENU"
            print "1 - View News"
            print "2 - Search Personalities"
            print "3 - Qualify News"
            print "4 - Most Influente Personalitie"
            print "5 - Most Influente Political Party"
            print "0 - Return to INTERFACE"

            menuoption = raw_input("Select an option: ")

            # OPCAO DE VER NOTICIAS DA PESQUISA
            if menuoption == "1":
                print 'VER NOTICIAS - IMPRIME TITULO, CONTEUDO, DATA'
                continue

            # OPCAO DE PESQUISAR PESSOAS
            elif menuoption == "2":
                print "PESQUISAR PESSOAS - IMPRIME TITULO, PESSOAS"
                continue

            # OPCAO DE CLASSIFICAR NOTICIA
            elif menuoption == "3":
                print "CLASSIFICAR NOTICIA - IMPRIME TITULO, CLASSIFICACAO"
                continue

            # OPCAO DE PESSOA MAIS INFLUENTE
            elif menuoption == "4":
                print "PESSOA MAIS INFLUENTE - IMPRIME PESSOA"
                continue

            # OPCAO DE PARTIDO MAIS INFLUENTE
            elif menuoption == "5":
                print "PARTIDO MAIS INFLUENTE - IMPRIME PARTIDO"
                continue

            # OPCAO DE SAIR
            elif menuoption == "0":
                break

            # OPCAO INVALIDA
            else:
                print "Invalid Input: Insert the option Number.\n"
                continue

    # OPCAO POR VER O HISTORICO
    elif option == "2":
        print 'HISTORY'
        print 'IMPRIME HISTORICO - WORDS, PESSOAS, PARTIDOS, MOST RELEVANT PERSON, MOST RELEVANT PARTY'

    # OPCAO SAIR 
    elif option == "0":
        break

    # OPCAO INVALIDA 
    else:
        print "Invalid Input: Insert the option Number.\n"
        continue

            