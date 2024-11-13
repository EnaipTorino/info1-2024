# la prossima volta proviamo http://www.flowgorithm.org/
soldi = 5
print("Scegli una bibita:")
print("1) Cherry cola 1$")
print("2) Ramune 2$")
print("3) Bubble tea 3$")
selezione = int(input("SELEZIONE: "))

if selezione == 1:
    print("hai scelto la cherry cola!")
    soldi = soldi - 1 
if selezione == 2:
    print("hai scelto la ramune!")
    soldi = soldi - 2
if selezione == 3:
    print("hai scelto il bubble tea!")
    soldi = soldi - 3

print("Hai ancora " + str(soldi) + "$")
