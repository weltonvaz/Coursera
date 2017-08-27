#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Escreva a função vogal que recebe um único caractere como parâmetro e devolve True
    se ele for uma vogal e False se for uma consoante."""

def vogal(s):
    if s.lower() in 'aeiou':
        return True
    else:
        return False
