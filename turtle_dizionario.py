import turtle

def nord(a, t):
    t.seth(90)
    t.forward(100)

def sud(a, t):
    t.seth(270)
    t.forward(100)

def est(a, t):
    t.seth(0)
    t.forward(100)

def ovest(a, t):
    t.seth(180)
    t.forward(100)

def main():
    A = 100
    dizionario ={"n": nord, "s":sud, "e":est, "o":ovest}
    operazione = input("Scrivi n per andare a nord, s per andare a sud, e per andare a est, o per andare a ovest : ")
    if operazione in dizionario:
        finestra = turtle.Screen()
        tarta = turtle.Turtle()
        print(dizionario[operazione](A, tarta))
    else:
        print("Errore")

        finestra.mainloop()

if __name__ == "__main__":
    main()