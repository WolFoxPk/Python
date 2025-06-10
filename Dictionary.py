# avendo la seguente lista di studenti

studenti = [
    ("Alice", 30), ("Bob", 28), ("Carla", 30),
    ("Daniele", 25), ("Elena", 28), ("Franco", 25)
]
# esegui l esercizio con questo output desiderato:
# {
#   30: ["Alice", "Carla"],
#   28: ["Bob", "Elena"],
#   25: ["Daniele", "Franco"]
# }
print()

nomi_raggruppati = {}

for nome, voto in studenti:
    if voto in nomi_raggruppati:
        nomi_raggruppati[voto].append(nome)
    else:
        nomi_raggruppati[voto] = [nome]

print(nomi_raggruppati)

print()

# e poi in questa altra lista,  conta delle lettere

dizionario={"nome": "Mario", "cognome": "Rossi", "eta": 30, "contatti":["email1","email2"]}

conteggio_lettere = {}

for valore in dizionario.values():
    if isinstance(valore, str):
        testo = valore
    elif isinstance(valore, list):
        testo = "".join([elem for elem in valore if isinstance(elem, str)])
    else:
        # continue  # ignora numeri o altri tipi
        testo = str(valore)

    for char in testo.lower():
        # if char.isalpha():  # stampiamo solo lettere
        if char.isalnum(): # stampiamo lettere e numeri
            conteggio_lettere[char] = conteggio_lettere.get(char, 0) + 1


for lettera in sorted(conteggio_lettere): # Stampa ordinata e alfabeticamente
    print(f"Lettera '{lettera.upper()}': {conteggio_lettere[lettera]} volta/e")

