#SLICING DI STRINGHE
s = "ciao" #l'ultimo carattere e -1
print(f"il primo carattere e' {s[0]}")
print(f"l'ultimo carattere e' {s[-1]}")
print(f"il penultimo carattere e' {s[-2]}")
print(f"l'ultimo carattere e' {s[len(s)-1]}")#C-style DA NON USARE

print(s[3:7]) #dal carattere 3 al carattere 7 escluso
print(s[1:-1])#stampa tutta la stringa tranne il primo e l'ultimo carattere
print(s[1:-])#tutta la stringa tranne il primo carattere
print(s[:-1])#tutta la stringa escluso l'ultimo carattere
# con :: stampa al contrario
