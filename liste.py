def print_list(l):
    print("La lista è: ", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def main():
    # Le liste
    l = [1, 2, 3, 4, "c", 3.14, "python"]
    r = [10, 11, 12]
    print_list(l+r) #concatenazione tra due liste
    print_list(3*r) #concatenazione multipla
    #print(l)
    #print(l[-1])
    #print(l[::-1]) # stampa al contrario

    #vogliamo permettere ad un utente di caricare una lista 
    lista = []
    num = 1
    while num>0
        num = int(input("scrivi un numero: (-1 per inter.): "))
        if num>0:
            lista.append(num)
            
    print_list(lista)

if __name__=="__main__":
        main()