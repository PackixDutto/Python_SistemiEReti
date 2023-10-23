import math


def calcola_distanza(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distanza = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distanza

def main():

x1 = float(input("Inserisci la coordinata x del primo punto: "))
y1 = float(input("Inserisci la coordinata y del primo punto: "))
x2 = float(input("Inserisci la coordinata x del secondo punto: "))
y2 = float(input("Inserisci la coordinata y del secondo punto: "))
punto1 = (x1, y1)
punto2 = (x2, y2)

distanza = calcola_distanza(punto1, punto2) #Calcola la distanza tra i due punti
print(f"La distanza tra i punti {punto1} e {punto2} è {distanza:.2f}")

if __name__ == "__main__":
    main()