import math

def mediaAritmetica(n1, n2):
    return (n1 + n2) / 2

def mediaGeometrica(n1, n2):
    return ()

def main():
    numero1 = int(input("inserisic il primo numero"))
    numero2 = int(input("inserisic il secondo numero"))
    dizionario = {"mediaAritmetica": mediaAritmetica(numero1, numero2), }
    print(dizionario)