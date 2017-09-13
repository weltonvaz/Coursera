#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro
   e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
"""

def isprime(n):
    fator = 2
    multiplicidade = 1

    while n > 1:
        while n % fator == 0:
           multiplicidade = multiplicidade + 1
           n = n / fator
        fator = fator + 1
    if multiplicidade == 2:
        return True
    else:
        return False

def n_primos(x):
    count = 1
    for i in range(3,x+1,2):
        if isprime(i) == True:
            count = count + 1
    return count

final = int(input("Digite o numero inteiro final: "))

print(n_primos(final))


    