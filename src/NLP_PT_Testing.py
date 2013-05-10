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
    for chunk in nltk.ne_chunk(changedlist):
        if hasattr(chunk, 'node') and chunk.node=="PERSON":
            returnlist.append(' '.join(c[0] for c in chunk.leaves()))
    print returnlist


def extractall_entities(text):
    words = token.compound_tokenizePT(text, "TB")
    for chunk in nltk.ne_chunk(nltk.pos_tag(words)):
        print chunk
            
        
def extractall_entities0(tagwords):
    for pos in tagwords:
        print pos
        
    
    
def main():
    
    print "---- FLORESTA POST TAG AUBT ----"
 
    text = u"O Amilcar é um camelo com duas bossas e muito pelo".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"A Angela é gorda e feia.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"Maria destestava apanhar sol.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_aubt(words)
    extractall_entities0(tagwords)
    
    print "---- FLORESTA POST TAG BRILL AUBT ----"
    
    text = u"O Amilcar é um camelo com duas bossas e muito pelo".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"Cavaco Silva reclama indignado com Passos Coelho. pois António José Seguro está a fazer caixinha.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"A Angela é gorda e feia.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"O ex-primeiro-ministro José Sócrates é um mentiroso.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    extractall_entities0(tagwords)
    
    text=u"Maria destestava apanhar sol.".encode('latin-1')
    words = token.compound_tokenizePT(text, "TB")
    tagwords = tagger.florestaPOStag_brill_aubt(words)
    extractall_entities0(tagwords)
    
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
    
    extractall_entities(text)
    
    print "NPROP no macmorpho é igual a NNP no pos_tag"
    
    extract_entitiesmac(text0)
    
    print "era necessário ter agora um chunk treinado com lingua portuguesa... para conseguir melhores resultados"
 
   
main()
