import turtle

def disegnaPoli(t, num, lato):
    gradi=360 / num
    t.begin_fill()
    for i in range(0, num):
            t.forward(lung)
            t.left(gradi)
            t.end_fill()

def posizionaTurtle(t, num, lato, x, y):
    t.penup()
    if(num%3 == 0):
        x = 100
        y = y + lato*4
    else:
        x = x + lato*4
    t.goto(x,y)
    t.pendown()


def main():
    x=0
    y=-100
    lung = int(input("inserire la lunghezza del lato: "))
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.shape("turtle") 
    tarta.color("red")
    tarta.speed("slow")


    for num in range(3,12):
        
            x, y=posizionaTurtle(tarta, num, lung, x, y)
            disegnaPoli(tarta, num, lung)
            

    finestra.mainloop() #mettilo sempre altrimenti non vedi la finestra 

if __name__=="__main__":
    main()