import turtle 

print ("dimmi il numero di facce della forma:\n")

facce = int (input())

print ("inserisci il colore della forma")
colore = input()

finestra = turtle.Screen()
packi = turtle.Turtle() #nome lo decidi tu

packi.speed(facce * 100)

packi.color(colore)

packi.fillcolor(colore)

packi.begin_fill() #inzia a riempire

for i in range(0, facce):
    
    packi.forward((350 + facce)/facce)
    packi.left(360/facce)

packi.end_fill()
    


finestra.mainloop() #mettilo sempre altrimenti non vedi la finestra 