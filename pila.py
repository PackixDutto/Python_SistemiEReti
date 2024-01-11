
def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    x=pila.pop()
    return x


def main():

    pila = [1,2,3,4]
    x = push(pila, 10)
    x = pop(pila)
    print(x, pila)

if __name__ == "__main__":
    main()

#pila.append(5)
#print(pila)
#x = pila.pop() !! lo accorcia di 1 
#print(x)
#print(pila)
