# -*- coding: utf-8 -*-
"""
Pergunte uma frase para o usuário e mostre todas as letras,
da mais frequente para a menos frequente, mostrando o número
de ocorrências.

Caso as letras possuam a mesma frequência, utilize a ordem 
alfabética.

* list: 1
* def: 1
"""

frase = input(">>> ").lower()

freqs = {}

for c in frase:
    freqs[c] = freqs.get(c, 0) + 1
    
def key_fn(par):
    letra, n = par
    return -n, letra

pares = sorted(freqs.items(), key=key_fn)


for c, n in pares:
    print(f"{c!r}: {n}")
