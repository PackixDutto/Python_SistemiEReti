#aprire e leggere un file e salvarlo dizionario

def main(): 

    rubrica = {}
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")
        #sostituisco \n con un carattere a scelta
        numeroTelefonico = (int(campi[1].replace("\n", "")))
        nome = campi[0]
        rubrica[numeroTelefonico] = nome
        #print(rubrica)

    print(rubrica)
    
if __name__ == "__main__":
    main()