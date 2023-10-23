#list compehension
#Lista con i primi 5 quadrati perfetti
import random
quadrati = [i*i for i in range (1, 6)]
numeri_interi = [i for i in range(1,11)]

stringhe = ["computer" , "cellulare" , "laptop"]

stringhe_c = [parola for parola in stringhe if parola[0] =="c"]
print(stringhe_c)

voti =  [random.randint(2, 10) for _ in range (0, 10)]
print(voti)
voti_insuf = [voto for voto in voti if voto <6]
print(voti_insuff)