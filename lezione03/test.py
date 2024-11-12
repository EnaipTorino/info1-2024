# contatori
spaventato = 0
gore = 0
zombie = 0
# Stampo la domanda
print("hai paura del buio?")
print("A) Sì")
print("B) No")
print("C) Brainssss!!")
# Ottengo la risposta
risposta = input("risposta")
# Valuto la risposta
if risposta == "A":
    spaventato = spaventato + 1
if risposta == "B":
    gore = gore + 1
if risposta == "C":
    zombie = zombie + 1
print(spaventato, risposta, zombie)