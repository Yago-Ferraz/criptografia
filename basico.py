import random

def gen():
    return random.randint(1,26)


def enc(m,k):
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    cifra='' 
    for letra in m:
        numero = alfabeto.index(letra)
        cifrado = (numero +k)%26
        cifra = cifra+alfabeto[cifrado]
    return cifra

print(enc('sdurj',-9))



def encascii(m,k):
    cifra='' 
    for letra in m:
        numero = ord(letra)
        cifrado = (numero +k)%128
        cifra = cifra+chr(cifrado)
    return cifra

