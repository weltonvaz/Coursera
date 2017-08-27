#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número
   primo menor ou igual ao número passado à função"""

from math import sqrt


def eprimo(x):
    euclides = int(sqrt(x))
    erato = 0
    count = 1
    for i in range(1, euclides + 1, 2):
        erato = divmod(x, i)
        if erato[1] == 0:
            count += 1
    if count <= 2:
        return True
    else:
        return False


def maior_primo(number):
    if eprimo(number) == True:
        return number
    else:
        for x in range((number - 1), 2,-1):
            if eprimo(x) == True:
                return x

