#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
"""Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
   Se o número for primo, imprima "primo". Caso contrário, imprima "não primo"."""

number = int(input("Digite um número inteiro: "))

count = 1
div = int(sqrt(number))

for y in range(0,div,2):
    if number % 2 == 0:
        count += 1

for x in range(1,div,2):
    if number % x == 0:
        count += 1

if count >= 3:
    print("não primo")
else:
    print("primo")
    