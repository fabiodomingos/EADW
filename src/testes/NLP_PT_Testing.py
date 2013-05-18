#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/05/10

to test and understand pos tag in portuguese words and trained taggers with florsta and mac_morpho

'''

import nltk
import NLP_PT

# instance of NLP_PT
token = NLP_PT.tokenizerPT()

# postagger
tagger = NLP_PT.POStagChunk()



def extract_entitiesmac(text):
    changedlist = []
    returnlist = []
    words = token.compound_tokenizePT(text, "TB")
    postag = tagger.macmorphoPOStag_aubt(words)
    for item in postag:
        if(item[1]=="NPROP"):
            changedlist.append((item[0],"NNP"))
        else:
            changedlist.append((item[0], item[1]))
    for chunk in nltk.ne_chunk(changedlist, binary=True):
        print chunk
        if hasattr(chunk, 'node') and chunk.node=="NE":
            returnlist.append(' '.join(c[0] for c in chunk.leaves()))
    print returnlist


def extractall_entities(text):
    words = token.compound_tokenizePT(text, "TB")
    for chunk in nltk.ne_chunk(nltk.pos_tag(words), binary=True):
        print chunk
            
        
def extractall_entities0(tagwords):
    for pos in tagwords:
        print pos
        
    
    
def main():
    
    print "---- FLORESTA POST TAG AUBT ----"

    text = u"O Amilcar é um camelo com duas bossas e muito pelo".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"A Angela é gorda e feia.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"Maria destestava apanhar sol.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    
    print "---- FLORESTA POST TAG BRILL AUBT ----"
    
    text = u"O Amilcar é um camelo com duas bossas e muito pelo".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"A Angela é gorda e feia.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------"
    
    text=u"Maria destestava apanhar sol.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    print tagwords
    print "------------------------------------------------------------------------------------------------------------" """
    
    print "---- MAC MORPHO AUBT ----"
    
    text = u"O Amilcar é um camelo com duas bossas e muito pelo."
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.macmorphoPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text0=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha."
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.macmorphoPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"A Angela é gorda e feia."
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.macmorphoPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso."
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.macmorphoPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"Maria detestava apanhar sol. O mau Manuel era bom."
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.macmorphoPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    print "com estes dados esta a dar bons resultados --- era preciso fazer match de NPROP para o utilizado pelo pos_tag"
    """
    """
    text0=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha."
    extractall_entities(text0)
    
    print "NPROP no macmorpho é igual a NNP no pos_tag"
    
    extract_entitiesmac(text0)
    
    text = u"O Amilcar é um camelo com duas bossas e muito pelo."
    extract_entitiesmac(text)
    
    text=u"A Angela é gorda e feia."
    extract_entitiesmac(text)
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso."
    extract_entitiesmac(text)
    
    text=u"Maria detestava apanhar sol. O mau Manuel era bom."
    extract_entitiesmac(text)
    
    print "era necessário ter agora um chunk treinado com lingua portuguesa... para conseguir melhores resultados" """
    
  #  catch = u"Em declarações à Antena 1, Manuel Alegre explica que não sabia de nada oficialmente:\"Soube há pouco tempo por intermédio do meu camarada António José Seguro que teria sido convocado o Conselho de Estado. Ele perguntou-se se eu tinha recebido a convocatória porque ele não tinha recebido até agora. Ora, não recebi. E fiquei a também saber que que o doutor Mário Soares também ainda não recebeu\". Esta é a décima reunião do Conselho de Estado, o órgão político de consulta do Presidente da República, desde que Cavaco Silva é chefe de Estado. A convocatória de Cavaco Silva surge um dia depois de o Governo ter aprovado as condições da contribuição de sustentabilidade do sistema de pensões, também chamada de \"TSU dos pensionistas\", numa reunião extraordinária do Conselho de Ministros, que confirmou as condições necessárias ao fecho da sétima avaliação da 'troika'."
 #   print ExtractNamedEntities.retrievePersonalities(catch)
    
 #   catch2 = u"Daniel Oliveira sublinhou, este sábado, na conferência \"Vencer a crise com o Estado Social e com a Democracia\", promovida pelo Congresso Democrático das Alternativas, no Fórum Lisboa, que não há muita margem de tempo para a ação e desafiou a Esquerda a unir-se para derrubar o Governo. \"O que perdermos nos próximos meses demorará décadas a reconstruir. Não nos sobra muito tempo. Por isso, se me perdoam a linguagem vulgar, fica o meu apelo: entendam-se porra!\", afirmou o antigo militante histórico do BE, colhendo aplausos na sala. Na intervenção que proferiu, e onde se referiu a Vítor Gaspar como \"o louco que dirige as Finanças\" e que vai aplicando cortes usando sempre o argumento de que não há dinheiro, sublinhou que \"os cortes só acabarão quando não houver mais nada para cortar\" e que, nessa altura, já \"não haverá dinheiro nem país\". A seu ver, destruir o Estado Social não é um programa de emergência para salvar o país, é o aproveitamento de uma oportunidade histórica para privatizar a democracia social\". Para Daniel Oliveira, \"este é o ajustamento desejado\", que \"ficará completo com um Estado Social caritativo e degradado\". Defendeu, por isso, que é necessário, quanto antes, renegociar a dívida e denunciar o memorando assinado com a troika\". As alternativas ao atual cenário, continuou, depende de duas condições: \"a demissão imediata do Governo que traiu os portugueses, com eleições antecipadas e a assunção por todas as oposições de que vivemos num momento de emergência nacional\"."
  #  print ExtractNamedEntities.retrievePersonalities(catch2)
    
 
   
main()




""" INTERFACE - POLITICS SEARCH
1 - New Search
2 - History
0 - Exit
Select an option: 1
Insert a word to search: desgraça
Searching...
Your search resulted in - 0 - news.



SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: debate
Invalid Input: Insert the option Number.



SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: 1
========== PRINTING ALL RESULTS ========
================ New ==============
>>TITLE
Uma semana negra
>>CONTENT
Vamos de mal a pior: a caminho da desgraça absoluta, se não houver uma mudança de política. A austeridade só serve os mercados usurários e a troika, criando cada vez mais de-sempregados e o empobrecimento geral, com as exceções conhecidas dos adeptos do Governo, porque esses vivem bem.
A nossa pátria está a ser destruída aos poucos mas sistematicamente, como a maioria esmagadora dos portugueses já percebeu, a começar pela fina flor do PSD e do CDS-PP, isto é, os mais conhecidos e respeitados. Como, por exemplo: Manuela Ferreira Leite, Pacheco Pereira, António Capucho e Rui Rio ou, do CDS-PP, Pires de Lima e Bagão Félix, sem esquecer a maioria dos autarcas, como se viu agora com o insuspeito Carlos Abreu Amorim, dado que não brincam quando as eleições se aproximam...
O Governo Passos Coelho está moribundo, como toda a gente já percebeu. Paralisado, sem rei nem roque nem qualquer estratégia coerente. Como é sabido, o poder efetivo depende do ministro das Finanças, Vítor Gaspar, um economicista fanático, que não é venal (ao que dizem) mas desconhece em absoluto as pessoas e o País em que nasceu. Só sabe de contas e cifrões. Não é ministro das Finanças, quando muito ministro do Orçamento!
Vítor Gaspar e Passos Coelho são uma dupla que se completa e impõe. Paulo Portas, líder do segundo partido da coligação, tem sido humilhado de várias formas. Basta dizer que é a terceira figura do Governo e não a segunda, como seria normal. Às vezes, parece querer impor-se, como aconteceu na semana passada. Puro bluff. O discurso que proferiu, com exigências ligeiras, não serviu para nada. Traçou uma linha vermelha que afinal não respeitou. Passos Coelho, meteu-o na ordem e humilhou-o de novo, no próprio Parlamento, para que ficasse claro. Tirou-lhe o tapete. Porque a ameaça de chantagem feita, discretamente, por Passos Coelho paralisa Portas.
Assim é a vida, com outras - e grandes - dificuldades com um Governo em que os ministros não se entendem entre si. Uns são discretos e não falam; outros não, como o ministro da Economia, que fala pelos cotovelos, mas ninguém o ouve, a começar por Gaspar e Coelho...
>>DATE
2013-05-14 01:15:00
Query: desgraça
In: 0 news


SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: 2
========== PRINTING ALL PERSONS ========
================ News ==============
>>TITLE
Uma semana negra
>>PERSONS
Manuela Ferreira Leite
José Pacheco Pereira
António Capucho
Rui Rio
António Pires de Lima
Carlos Abreu Amorim
Pedro Passos Coelho
Paulo Portas
Query: desgraça
In: 0 news


SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: 4
========== MOST POPULAR POLITICIAN =========
Pedro Passos Coelho


SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: 5
========== MOST POPULAR PARTY ==========
PSD


SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option: 6
========== PRINTING ALL PERSONS ========
================ News ==============
>>TITLE
Uma semana negra
>>QUALIFY
NOTICIA NEGATIVA
None


SEARCH MENU
1 - View News
2 - View Politicians (by News Title)
3 - View Politicians (search resume)
4 - Most Popular Politician
5 - Most Popular Political Party
6 - Qualify News
0 - Return to INTERFACE
Select an option:  """
