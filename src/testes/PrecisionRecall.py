#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

Test: precision and recall


'''
import json

"""
#A = retrieved objects (set)
#R = relevant objects (set)
"""

# ## PRECISION FORMULA

def precision(A, R):
    """ is the proportion of retrieved objects that are relevant """
    A = set(A)
    R = set(R)
    intersectionAR = A.intersection(R)
    return float(len(intersectionAR)) / float(len(A))

def precisionT(A, R):
    sum = 0
    for i,a in enumerate(A):
        sum = sum + precision(a, R[i])
    print round(sum/i * 100, 2)

# ## RECALL FORMULA

def recall(A, R):
    """ is the proportion of relevant objects retrieved """
    A = set(A)
    R = set(R)
    intersectionAR = A.intersection(R)
    return float(len(intersectionAR)) / float(len(R))

def recallT(A, R):
    sum = 0
    for i,a in enumerate(A):
        sum = sum + recall(a, R[i])
    print round(sum/i * 100, 2)


#############################################
########### NAMED ENTITIES ##################
#############################################

# ## CONSTRUCTING A - retrieved objects from 8 news

def nameEntities():
    A_step1 = json.load(open("politicians_test.txt"))
    A_step2 = []
    for k in A_step1:
        itera = A_step1[k][0]
        while (iter != 0):
            A_step2.append(k.join(iter))
            itera = iter - 1
    print A_step2
    
# ## CONTRUCTING R - manual observations from 8 news

R_step1 = [u"Pedro Passos Coelho1", u"Paulo Portas1", u"Pedro Passos Coelho2", u"Aníbal Cavaco Silva1", u"Miguel Maduro1",
           u"Jerónimo de Sousa1", u"Aníbal Cavaco Silva2", u"Jerónimo de Sousa2", u"Pedro Passos Coelho3", u"Paulo Portas2",
           u"António José Seguro1", u"Paulo Portas3", u"Paulo Neves1",
           u"Pedro Passos Coelho4", u"Paulo Portas4"
           u"Pedro Passos Coelho5", u"Paulo Portas5", u"Jerónimo de Sousa3", u"Aníbal Cavaco Silva3", u"Jerónimo de Sousa3", u"Pedro Passos Coelho6", u"Paulo Portas6",
           u"Paulo Portas7", u"Mário Soares1", u"Paulo Portas8", "Carlos Mota Pinto1",
           u"Paulo Portas8", u"Paulo Portas9",
           u"Paulo Portas10", u"Morais Sarmento1", u"Paulo Portas11", u"Pedro Passos Coelho7", u"Vítor Gaspar1", u"Carlos Moedas1", u"Paulo Portas12"]
           

# ## CONTRUCTING A FROM 8 news - retrieved objects 
A_step1 = [[u"Pedro Passos Coelho",u"Aníbal Cavaco Silva"], 
           [u"Jerónimo de Sousa", u"Aníbal Cavaco Silva", u"Pedro Passos Coelho", u"Paulo Portas"],
           [u"António José Seguro", u"Paulo Portas", u"Paulo Neves"],
           [u"Pedro Passos Coelho", u"Paulo Portas"],
           [u"Pedro Passos Coelho", u"Paulo Portas", u"Jerónimo de Sousa", u"Aníbal Cavaco Silva"],
           [u"Paulo Portas", u"Carlos Mota Pinto", u"Paulo Mota Pinto"],
           [u"Paulo Portas"],
           [u"Paulo Portas", u"Nuno Morais Sarmento", u"Pedro Passos Coelho"]]
           
# ## CONSTRUCTING R from 8 news - relevant objects manualy observed
R_step1 = [[u"Pedro Passos Coelho", u"Paulo Portas", u"Aníbal Cavaco Silva1", u"Miguel Maduro"],
           [u"Jerónimo de Sousa", u"Aníbal Cavaco Silva2", u"Pedro Passos Coelho", u"Paulo Portas"],
           [u"António José Seguro", u"Paulo Portas", u"Paulo Neves"],
           [u"Pedro Passos Coelho", u"Paulo Portas"],
           [u"Pedro Passos Coelho", u"Paulo Portas", u"Jerónimo de Sousa", u"Aníbal Cavaco Silva"],
           [u"Paulo Portas", u"Mário Soares","Carlos Mota Pinto"],
           [u"Paulo Portas"],
           [u"Paulo Portas", u"Morais Sarmento", u"Pedro Passos Coelho7", u"Vítor Gaspar", u"Carlos Moedas"]]

# ## CALCULATIONS
# PRECISION
print "PRECISION FOR NAMED ENTITIES:"
precisionT(A_step1, R_step1)
# RECALL
print "RECALL FOR NAMED ENTITIES:"
recallT(A_step1, R_step1)


#####################################
############ QUALIFYING #############
#####################################

A_step1 = ["negativa1", "neutra1", "positiva1", "positiva2", "positiva3", "negativa2", "positiva4", "negativa3"]
R_step1 = ["negativa1", "neutra1", "negativa2", "negativa3", "positiva1", "negativa4", "negativa5", "negativa6"]

A_step1 = ["negativa", "neutra", "positiva", "positiva", "positiva", "negativa", "positiva", "negativa"]
R_step1 = ["negativa", "neutra", "negativa", "negativa", "positiva", "negativa", "negativa", "negativa"]

# ## CALCULATIONS
# PRECISION
print "PRECISION FOR QUALIFYING - NEWS:"
precisionT(A_step1, R_step1)
# RECALL
print "RECALL FOR QUALIFYING - NEWS:"
recallT(A_step1, R_step1)


## Morais sarmento : positivo vs neutro
## Paulo Portas : positivo vs positivo


