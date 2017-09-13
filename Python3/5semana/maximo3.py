#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles."""

def maximo(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return x

#print(maximo(0,-1, 1) )



