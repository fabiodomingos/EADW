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

# FUN‚ÌO MENU SEARCH QUE CONTEM AS OP‚ÍES DENTRO DE UMA PESQUISA
def menuSearch(search):
    NewsSearch.searchByRelevance(search)
    while(1):
        print "MENU SEARCH"
        print "1 - Search Personalities"
        print "2- Qualify News"
        print "3 - Most Relevant Personalitie"
        print "0 - Return to Main Menu"
        
        option = raw_input("Select an option: ")
        
        if option == "1":
            NewsSearch.searchByPersonalitie(search)
            continue
        
        elif option == "2":
            NewsSearch.searchByQualify(search, sentilexDic)
            continue
        
        elif option == "3":
            print "FAZER FUN‚ÌO PARA A PERSONALIDADE MAIS RELEVANTE"
            continue
        
        elif option == "0":
            return
        
        else:
            print "Invalid Input: Insert the option Number.\n"
            continue
            
        
# FUN‚ÌO MENU PRINCIPAL ONDE ESTÌO AS OP‚ÍES DE ADICIONAR NOVAS NOTICIAS OU PESQUISAR NAS NOTICIAS    
def menuPrincipal():
    while(1):
        print "MENU PRINCIPAL"
        print "1 - Collect new News"
        print "2 - Search in the News"
        print "3 - Exit"
            
        option = raw_input("Select an option: ")
    
        if option == "1":
            print "Tem ao seu dipor o JN e o DN"
            feed = raw_input("Select your Newspaper: ")
            if feed=="DN":
                print "PENSAR COMO FAZER O COLLECT"
                continue
            elif feed=="JN":
                print "PENSAR COMO FAZER O COLLECT"
                continue
            else:
                print "Invalid Input: You need to choose JN or DN"
        
        elif option == "2":
            search = raw_input("Find news with word: ")
            menuSearch(search)
        
        elif option == "3":
            return
        
        else:
            print "Invalid Input: Insert the option Number.\n"
            continue
            
def main():
    # VAI ARRANCAR A INTERFACE COM AS OP‚ÍES DE USAR UMA DB EXISTENTE OU CRIAR UMA NOVA DB 
    while(1):
        print "DATA MINING - INTERFACE"
        print "1 - Use a DB system"
        print "2 - Create a new DB"
    
        option = raw_input("Select an option: ")
    
        if option == "1":
            print "FALTA FAZER IR BUSCAR VARIAS DB E CHAMA MENU PRINCIPAL "
            menuPrincipal()
            break
        
        elif option == "2":
            print "FALTA CRIAR NOVA DB E CHAMA MENU PRINCIPAL"
            menuPrincipal()
            break
        
        else:
            print "Invalid Input: Insert the option Number.\n"
            continue

            
            