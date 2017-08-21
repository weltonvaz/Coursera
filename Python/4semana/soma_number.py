#!/usr/bin/env python3
# -*- coding: utf-8 -*-

number = input("Digite um número inteiro: ")
count = 0

for x in number:
    count = count + int(x)

print(count)