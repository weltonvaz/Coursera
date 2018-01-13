#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Digite vários números e imprima os números invertidos.
"""
numbers = []

while True:
    n = int(input("Digite um número: "))
    if n != 0:
        numbers.append(n)
    else:
        break
print(numbers[::-1])