#!/usr/bin/env python3

"""fuzzy.py: Exercícios 2 - FizzBuzz parcial, parte 1 - Receba um número inteiro na entrada e imprima"""

__author__      = "Welton Vaz"
__copyleft__   = "Copyright 2017, Planet Earth"

number = int(input("Digite um numero: "))

if number % 5 == 0:
    print('Buzz')
else:
    print(number)