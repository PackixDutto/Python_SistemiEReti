def main():

    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))

    quadrato_numero1 = numero1 ** 2 #quadrati dei due numeri
    quadrato_numero2 = numero2 ** 2

    quadrato_somma = (numero1 + numero2) ** 2 #quadrato della somma dei numeri

    differenza_quadrati = quadrato_numero1 - quadrato_numero2 #differenza tra i quadrati dei due numeri

    quadrato_differenza = (numero1 - numero2) ** 2 #quadrato della differenza tra i numeri

    risultati = [quadrato_numero1 + quadrato_numero2, quadrato_somma, differenza_quadrati, quadrato_differenza] #lista contenente i risultati

    print("Lista dei risultati:") #stampa la lista ottenuta
    print(risultati)

if __name__ == "__main__":
    main()