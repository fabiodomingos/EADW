'''
Created on 2013/05/05

@author: goncalocarito, fabiodomingos
'''

import nltk
from nltk.corpus import floresta
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer

class POStagChunk:
    '''
    classdocs
    '''

    tagger_brill_aubt = nltk.data.load("taggers/floresta_brill_aubt.pickle")
    tagger_aubt = nltk.data.load("taggers/floresta_aubt.pickle")
    tagger_ubt = nltk.data.load('taggers/floresta_ubt.pickle')
    tagger_brill_ubt = nltk.data.load('taggers/floresta_brill_ubt.pickle')

    def __init__(self,listofwords):
        '''
        Constructor
        '''
        self.listofwords = listofwords
        
    def defaultPOStagChunk(self):
        return nltk.ne_chunk(nltk.pos_tag(self.listofwords))
    
    def florestaPOStag(self, tagger):
        return tagger.tag(self.listofwords)
    
    def florestaPOStag_brill_aubt(self, tagger = tagger_brill_aubt):
        return self.florestaPOStag(tagger)
    
    def florestaPOStag_aubt(self, tagger = tagger_aubt):
        return self.florestaPOStag(tagger)
    
    def florestaPOStag_ubt(self, tagger = tagger_ubt):
        return self.florestaPOStag(tagger) 
    
    def florestaPOStag_ubt_brill(self, tagger = tagger_brill_ubt):
        return self.florestaPOStag(tagger) 
    
#    def evaluatePOStag(self, tagger, corpus):
#        return tagger.evaluate(corpus)
    
class tokenizerPT():
    
   # def __init__(self, text):
   #     self.text = text
    
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
        """ for use combiantion or original tokenizers 
            @output: list with all words """
        outputlist = []
        for sent in self.sent_tokenizeEN(text):
            for word in self.word_tokenizeEN(sent):
                outputlist.append(word)
        return outputlist
    
    def special_tokenizerEN(self, text):
        outputdict = {}
        i = 0
        for sent in self.sent_tokenizeEN(text):
            for word in self.word_tokenizeEN(sent):
                outputdict.update({word: i})
                i = i + 1
        return outputdict
    
        
    
    
    