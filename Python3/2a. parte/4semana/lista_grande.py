"""Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro
n e devolve uma lista contendo n números inteiros aleatórios."""
from random import randint

def lista_grande(n):
    if n == 0:
        listag = []
        return listag
    else:
        listag = [n]
        for x in range(0,n-1):
            listag.append(randint(n+1,n**2))
        return listag
    