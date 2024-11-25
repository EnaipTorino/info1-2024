nome = "Mattia"
print(nome + "!!") # concateno (stampa 'Mattia!!')
print(len(nome))
print(nome.upper())

# Python è case sensitive:
if nome == "mattia":
    print("python")


nomeMaiuscolo = nome.upper()
# Python è case sensitive:
if nome == "MATTIA":
    print("python")

# https://www.w3schools.com/python/python_strings_modify.asp


testo = "Questo è un testo"
lunghezza = len(testo)
print(testo[0])
print(testo[1])
print(testo[3])
print(testo[lunghezza - 1]) # stampo l'ultima lettera
print(testo[1:8]) # stampo un intervallo
print(testo[6:])
## -1 rappresenta penultima lettera
print(testo[-5:])

