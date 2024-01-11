import random

def movimento_casuale():
    return random.scelta([-1, 1])

def main():

    spostamenti_casuali = [movimento_casuale() for _ in range(5 * 24 * 60 * 60)] #giorni tot ore tot minuti tot secondi tot
    spostamento_totale = 0
    for spostamento in spostamenti_casuali:
        spostamento_totale = spostamento_totale + spostamento

    print(f"spostamento tot in 5 giorni {spostamento_totale}")
if _name_ == "_main_":
    main()