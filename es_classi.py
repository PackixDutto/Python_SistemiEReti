class Quadrato():   #costruttore
    def __init__(self, lato): #per ogni classe fai il suo init
        self.lato = lato

    def calcolaArea(self):
        return self.lato**2

    def stampaLato(self):
        print(f"il lato è {self.lato}")

def main():
    q=Quadrato(4)
    print(f"L'area del quadrato q è {q.calcolaArea}")
    print(q.lato)
    1.lato = 5
    print(f"L'area del quadrato q è {q.calcolaArea}")