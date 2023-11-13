#il dizionario e una collezione di coppie chiave: valore
#il dizionario non ha indici ma si indiciza 
#per chiave

#la chiave puo essere di un solo tipo #questo dizionario contiene 2 elementi ovvero 2 coppie, io se voglio un elemento lo indicizzo come chiave
dizionari = {"nome": "Mario", "cognome": "Rossi"} #la posizione diventa cio che tu vuoi
#lista = ["Mario", "Rossi"]   lista che e simile al dizionario
print(dizionario"[nome]") 

#aggiunge due elementi nuovi
dizionario["data nascita"] = "01/01/1900"
dizionario["età"] = 123

#sovrascrivere l'elemento con chiave "nome"
dizionario["nome"] = "Luca"

print(dizionario)

#ciclo for su dizionario 1
for chiave in dizionario:
    print(f" Chiave: {chiave} - valore : {dizionario[chiave]}")

rubrica = {38189192: "Mario Rossi", 348039013: "Alice Verdi"
           32193991: "Luca Gialli"}