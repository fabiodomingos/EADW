'''
Created on 2013/04/05

@author: goncalocarito
'''
import whoosh

filename="aula03_cfc.txt"
from whoosh.index import create_in 
from whoosh.fields import *

def makeindex():
    schema = Schema(id = NUMERIC(stored=True), content=TEXT) 
    ix = create_in("indexdir", schema) 
    writer = ix.writer()
    with open(filename,'r') as f:
        for line in f:
            writer.add_document(id=line[:5], content=line[6:].decode('latin-1'))
    writer.commit()

#uncomment de followed line to create a new index
# indexdir should exists previously
makeindex()
raw_input("INDEX CREATED - click to continue")


