import pandas 
import csv
import os


escrita = csv.writer(open("falas.txt", "wb"))

c = ['Nome','teste']


def DialogoInicial():
    
    entrada = input("Seu nome: ")
    
    nome = entrada

    c.append(nome)

DialogoInicial()