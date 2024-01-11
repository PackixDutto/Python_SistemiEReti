def push(pila, elemento):
    pila.append(elemento)


def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x


def main():
    stringa = "{[(]}"
    parentesi_aperte = ["{", "[", "("]
    parentesi_chiuse = ["}", "]", ")"]
    dizionario = {"{": "}", "[": "]", "(": ")"}
    stringa="([])"
    pila = []
    errore = False
    k = 0
    posErrore = null
    for poscarattere, carattere in enumerate(stringa):
        if carattere in parentesi_aperte:
            push(pila, carattere)
            k=k+1
        if carattere in parentesi_chiuse:
            if a > 0:
            parentesi = pop(pila)
            if parentesi is not None: 
                if dizionario[parentesi] != carattere:
                    errore = True
                    posErrore=poscarattere
                    else:
                        a-=1
                else:
                    errore = True
                    posErrore=poscarattere
            else:
               errore = True
               posErrore=poscarattere

    if errore or a>0:
        print(f"Errore all'indice {k}")
    else:
        print("Giusta")


if _name_ == "_main_":
    main()