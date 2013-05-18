'''

@author: goncalocarito & fabiodomingos

This is a module to create a sentilex.txt file that saves a python dict from SentiLex-PT02 with words as key and sentiment as values
0: neutral
1: positive
-1: negative

'''
import json

filename = 'SentiLex-PT02/SentiLex-lem-PT02.txt'

print "...."

def extractSentilex(Sentilex):
    sentilexDic={}
    with open(Sentilex, 'r') as f:
        for line in f:
            lineWords=line.split(';')
            palavra=lineWords[0].split('.')[0]
            sentimento=lineWords[2].split('=')[1]
            sentilexDic.update({palavra.decode('utf-8'):sentimento})
    return sentilexDic

senti = extractSentilex(filename)

json.dump(senti, open("sentilex.txt", 'w'))

print "sentilex.txt was created in this dir."