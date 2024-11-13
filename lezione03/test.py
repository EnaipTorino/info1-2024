# contatori
spaventato = 0
gore = 0
zombie = 0
# Stampo la domanda
print("hai paura del buio?")
print("a) Sì")
print("b) No")
print("c) Brainssss!!")
# Ottengo la risposta
risposta = input("risposta")
# Valuto la risposta
if risposta == "a":
    spaventato = spaventato + 1
if risposta == "b":
    gore = gore + 1
if risposta == "c":
    zombie = zombie + 1


# Stampo la domanda
print("Ti piacciono i cervelli?")
print("a) Sì")
print("b) No")
print("c) Brainssss!!")
# Ottengo la risposta
risposta = input("risposta")
# Valuto la risposta
if risposta == "a":
    zombie = zombie + 1
if risposta == "b":
    spaventato = spaventato + 1
if risposta == "c":
    zombie = zombie + 2
print(spaventato, gore, zombie)
'''
if zombie > spaventato:
    print("Ti consiglio the walking dead")
else:
    print("Ti consiglio peppa pig")
'''
'''
a = 0
b = 1
c = 2

# massimo tra a, b e c
if a>b:
    if a>c:
        print("a è il maggiore")
    else:
        print("c è il maggiore")
else:
    if b>c:
        print("a è il maggiore")
    else:
        print("c è il maggiore")  
'''
a = 0
b = 1
c = 2

if a>b:
    if a>c:
        print("a è il maggiore")
    else:
        print("c è il maggiore")
else:
    if b>c:
        print("a è il maggiore")
    else:
        print("c è il maggiore")  
