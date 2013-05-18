#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2013/05/05

@author: goncalocarito, fabiodomingos

Natural Language Processing in Portuguese. 
Classes.

'''

import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords

class POStagChunk:
    '''
    class with function for pos_tag and chunk
    essencialy pos_tag with trained taggers with portuguese corpus 
    '''

    tagger_brill_aubt = nltk.data.load("taggers/floresta_brill_aubt.pickle")
    tagger_aubt = nltk.data.load("taggers/floresta_aubt.pickle")
    tagger_ubt = nltk.data.load('taggers/floresta_ubt.pickle')
    tagger_brill_ubt = nltk.data.load('taggers/floresta_brill_ubt.pickle')
    tagger_aubt_morpho_sample = nltk.data.load('taggers/mac_morpho_aubt_sample.pickle') # just one sample file
    tagger_aubt_morpho = nltk.data.load('taggers/mac_morpho_aubt.pickle') # 50% of mac_morpho corpus

        
    def defaultPOStagChunk(self, listofwords):
        """ default nltk pos_tag and ne_chunk """
        return nltk.ne_chunk(nltk.pos_tag(listofwords))
    
    def florestaPOStag(self, listofwords, tagger):
        """ apply the pos tagger trained with floresta to a list of words (general)
        @input: receives the tagger 
        @return: tagged list (a tuple with word, pos tag) in each position """
        return tagger.tag(listofwords)
    
    def florestaPOStag_brill_aubt(self, listofwords, tagger = tagger_brill_aubt):
        """ specification for brill, Affix, Unigram, Bigram, Trigram training """
        return self.florestaPOStag(listofwords, tagger)
    
    def florestaPOStag_aubt(self, listofwords, tagger = tagger_aubt):
        """ specification for Affix, Unigram, Bigram, Tigram training """
        return self.florestaPOStag(listofwords, tagger)
    
    def florestaPOStag_ubt(self, listofwords, tagger = tagger_ubt):
        """ specification for Unigram, Bigram, Tigram training """
        return self.florestaPOStag(listofwords, tagger) 
    
    def florestaPOStag_brill_ubt(self, listofwords, tagger = tagger_brill_ubt):
        """ specification for brill, Unigram, Bigram, Trigram """
        return self.florestaPOStag(listofwords, tagger)
    
    def macmorphoPOStag(self, listofwords, tagger):
        return tagger.tag(listofwords)
    
    def macmorphoPOStag_aubt(self, listofwords, tagger = tagger_aubt_morpho):
        return self.macmorphoPOStag(listofwords, tagger)
    
    def macmorphoPOStag_aubt_sample(self, listofwords, tagger = tagger_aubt_morpho_sample):
        return self.macmorphoPOStag(listofwords, tagger)
    
    
    
    
class tokenizerPT():
    '''
    functions for tokenizer of portuguese texts, sentences, words 
    '''
    
    def sent_tokenizePT(self, text):
        """ sent_tokenizerPT tokenize sentences in portuguese language
            @input: string text with i.e. news (self)
            @returns: list of sentences """
        tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
        return tokenizer.tokenize(text)   
    
    def word_tokenizePT(self,  text, tokenizer):
        """ tokenize a portuguese sentence in words
        @input params: sentence - a sentence, a phrase (self)
                       tokenizer - "TB" for TreebankWordTokenizer
                                   "WP" for WordPunctTokenizer
        @returns word's list or error """
        if tokenizer == "TB":
            tokenizerTB = TreebankWordTokenizer()
            return tokenizerTB.tokenize(text)
        elif tokenizer == "WP":
            tokenizerWP = WordPunctTokenizer()
            return tokenizerWP.tokenize(text)
        else:
            return "tokenizer error: not found" 
        
    def compound_tokenizePT(self, text, tokenizer):
        """ for use combination of sent_tokinzerPT and word_tokenizerPT together
            @output: list with all words """
        outputlist = []
        for sent in self.sent_tokenizePT(text):
            for word in self.word_tokenizePT(sent, tokenizer):
                outputlist.append(word)
        return outputlist
    
    def sent_tokenizeEN(self, text):
        """ the original sent_tokenizer optimized for english words """
        return nltk.sent_tokenize(text)
    
    def word_tokenizeEN(self, text):
        """ the original word_tokenizer optimized for english words """
        return nltk.word_tokenize(text)

    def compound_tokenizeEN(self, text):
        """ for use combination or original tokenizers 
            @output: list with all words """
        outputlist = []
        for sent in self.sent_tokenizeEN(text):
            for word in self.word_tokenizeEN(sent):
                outputlist.append(word)
        return outputlist
    
    def special_tokenizerEN(self, text):
        """ retrieves a dictionary with indicies for each word """
        outputdict = {}
        i = 0
        for sent in self.sent_tokenizeEN(text):
            for word in self.word_tokenizeEN(sent):
                outputdict.update({word: i})
                i = i + 1
        return outputdict

    def special_tokenizerPT(self, text):
        """ retrieves a dictionary with indicies for each word """
        outputdict = {}
        i = 0
        for sent in self.sent_tokenizeEN(text):
            for word in self.word_tokenizeEN(sent):
                outputdict.update({i: word})
                i = i + 1
        return outputdict
    
    def filterStopsList(self, text):
        """ discard symbols and words that are not used for
        natural language processing.
        @input: string text
        @returns: a list with all of the words remaining after filters' application """
        portuguese_stops = stopwords.words('portuguese')
        STOPS=portuguese_stops+['.',',',':',';','-']
        words = self.compound_tokenizePT(text, "TB")
        filtro=[]
        filtroSentence=[word for word in words if word not in STOPS]
        filtro=filtro+filtroSentence
        return filtro
    
    def filterStopsSet(self, text):
        return set(self.filterStopsList(text))
    
        
#    def evaluatePOStag(self, tagger, corpus):
#        return tagger.evaluate(corpus)
    
    