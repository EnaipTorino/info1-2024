# input restituisce un testo
tempTesto = input("inserisci la temperatura: ")
# converto il testo in numero
temp = int(tempTesto)
if temp > 25:
    print("Fa caldo")
else:
    print("Fa freddo")
