# -*- coding: utf-8 -*-
"""
Crie um programa que leia um número n e retorne a sequência de Fizz-Buzz até este número.

A sequência Fizz-Buzz é feita imprimindo cada número natural, mas trocando os múltiplos 
de 3 por "fizz", os múltiplos de 5 por "buzz" e os múltiplos de ambos por "fizzbuzz".

* for: 1
* if: 1
"""

n = int(input(("n: ")))

for i in range(1,n + 1):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
