#!/usr/bin/env python3

"""Verifiordenacao.py: Exercício 5 - Verificando ordenação - Receba 3 números inteiros na entrada e imprima"""

__author__ = "Welton Vaz"
__copyleft__ = "Copyright 2017, Planet Earth"

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número : "))
number3 = int(input("Digite o terceiro número: "))

if number1 < number2 < number3:
    print("crescente")
else:
    print("não está em ordem crescente")
