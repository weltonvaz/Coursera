#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito
   com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não"."""

number = input("Digite um número: ")

count = 0

for x in range(0,len(number)):
    word = (number[x] + number[x])
    if  number.count(word):
        count +=1

if count >= 1:
    print("sim")
else:
    print("não")