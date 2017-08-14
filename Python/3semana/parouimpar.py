#!/usr/bin/env python3

"""parouimpar.py: Exercício 1 - Par ou ímpar? Receba um número inteiro na entrada e imprima."""

__author__      = "Welton Vaz"
__copyleft__   = "Copyright 2017, Planet Earth"

number = int(input("Digite um numero: "))

if number % 2 == 0:
    print('par')
else:
    print('ímpar')