import turtle

def Padding(Stringa):
    if len(self.nome)

def BarCode(tarta, StringaBin):
    turtle.pensize(4)
    n = 0
    for i in range(len(StringaBin)):
        if StringaBin[i] == '1':
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()
            n += 4
        else:
            n += 4


def main():
    Stringa = []
    for k in range(8):
        n = input("Inserisci il carattere: ")
        if ord(n) <=255:
            Stringa.append(ord(n))
        else:
            print("Carattere non valido")
    
    tarta = turtle.Turtle()
    finestra = turtle.Screen()
    for k in range(8):
        BarCode(tarta, bin(Stringa[k]))
    
    turtle.mainloop()

if __name__ == "__main__":
    main()