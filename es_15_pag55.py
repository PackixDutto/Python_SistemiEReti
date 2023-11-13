def main():

    nome = input("Inserisci il tuo nome: ")
    nome_ = nome[0] + '*' * (len(nome) - 1) #Sostituisci tutti i caratteri tranne il primo con '*'
    print("Nome con solo il primo carattere:", nome_)

if __name__ == "__main__":
    main()