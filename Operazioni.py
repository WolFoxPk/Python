from math import sqrt, exp
# import math
#
# print("---------CALCOLATRICE----------------")
#
#
# def somma(a, b):
#     return a + b
#
# def sottrazione(a, b):
#     return a - b
#
# def moltiplicazione(a, b):
#     return a * b
#
# def divisione(a, b):
#     return a / b
#
# def esponente(a, b):
#     return a ** b
#
# def radice_quadrata(a):
#     return math.sqrt(a)
#
# def somma_lista():
#     print("Inserisci numeri da sommare e poi premi 'i' per interrompere ed eseguire l operazione: ")
#     lista = []
#     while True:
#         num = input()
#         if num.lower() == 'i':
#             break
#         try:
#             num = float(num)
#             lista.append(num)
#         except ValueError:
#             print("Errore: inserire un numero valido.")
#     return sum(lista)
#
#
# print("Scegli un operazione da utilizzare tra quelle presenti: +, -, *, /, ** (esponente), sqrt (radice quadrata), l (somma lista)")
#
# while True:
#     operazione = input("Inserisci l operatorazione che hai scelto (+, -, *, /, **, sqrt, l) o 'q' per uscire: ").strip()
#
#     if operazione.lower() == 'q':
#         print("Chiusura della calcolatrice.")
#         break
#
#     if operazione == "l":
#         risultato = somma_lista()
#         print(f"Risultato: {risultato}\n")
#         continue
#
#     if operazione == "sqrt":
#         num = input("Inserisci un numero: ")
#         try:
#             num = float(num)
#             if num < 0:
#                 print("Errore: radice quadrata di numero negativo.")
#                 continue
#             risultato = radice_quadrata(num)
#             print(f"Risultato: {risultato}\n")
#         except ValueError:
#             print("Errore: inserire un numero valido.")
#         continue
#
#     if operazione == "":
#         num1 = input("Inserisci il primo numero: ")
#         num2 = input("Inserisci il secondo numero: ")
#         try:
#             num1 = float(num1)
#             num2 = float(num2)
#             risultato = esponente(num1, num2)
#             print(f"Risultato: {risultato}\n")
#         except ValueError:
#             print("Errore: inserire un numero valido.")
#         continue
#
#     num1 = input("Inserisci il primo numero: ")
#     num2 = input("Inserisci il secondo numero: ")
#
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#     except ValueError:
#         print("Errore: inserire un numero valido.")
#         continue
#
#     if operazione == "+":
#         risultato = somma(num1, num2)
#     elif operazione == "-":
#         risultato = sottrazione(num1, num2)
#     elif operazione == "*":
#         risultato = moltiplicazione(num1, num2)
#     elif operazione == "/":
#         risultato = divisione(num1, num2)
#     else:
#         print("Operazione non valida.")
#         continue
#
#     print(f"Risultato: {risultato}\n")

#---------------------------------- È POSSIBILE FARE ANCHE UN ALTRO MODO SENZA LISTA ----------------------------------

def leggi_numero(prompt, tentativi_max=5):
    tentativi= 0
    while tentativi < tentativi_max:
        try:
            return float(input(prompt))
        except ValueError:
            tentativi += 1
            print(f"Non hai inserito un numero. Inserisci un numero valido. Tentativi rimasti: {tentativi_max - tentativi}")
    print("Hai esaurito i tuoi tentativi. Il programma si autodistruggerà in pochi secondi. Buona vita!")
    exit()


def addizione():
    num1 = leggi_numero("Inserisci un numero: ")
    num2 = leggi_numero("Inserisci un secondo numero: ")
    risultato = num1 + num2
    print("Il risultato della tua addizione è: ", risultato)

def sottrazione():
    num1 = leggi_numero("Inserisci un numero: ")
    num2 = leggi_numero("Inserisci un secondo numero: ")
    risultato = num1 - num2
    print("Il risultato della tua sottrazione è: ", risultato)

def multipliczione():
    num1 = leggi_numero("Inserisci un numero: ")
    num2 = leggi_numero("Inserisci un secondo numero: ")
    risultato = num1 * num2
    print("Il risultato della tua moltiplicazione è: ", risultato)

def divisione():
    num1 = leggi_numero("Inserisci un numero: ")
    num2 = leggi_numero("Inserisci un secondo numero (questo non può essere zero): ")
    if num2 == 0:
        print("Errore! Il numero non può essere divisibile per 0(zero).")
    else:
        risultato = num1 / num2
        print("Il risultato della tua divisione è: ", risultato)


def esponenza():
    num1 = leggi_numero("Inserisci l esponente: ")
    risultato = exp(num1)
    print("Il risultato del calcolo esponenziale è: ", risultato)

def radiceQ():
    num1 = leggi_numero("Inserisci il numero di cui vuoi calcolare la radice quadrata: ")
    if num1 < 0:
        print("Errore: impossibile calcolare la radice di un numero negativo.")
    else:
        risultato = sqrt(num1)
        print("La radice quadrata di", num1, "è:", risultato)

def somma_lista():
    print("Inserisci numeri da sommare e/o premi 'i' per interrompere ed eseguire l operazione: ")
    lista = []
    while True:
        valore = input()
        if valore.lower() == 'i':
            break
        try:
            num = float(valore)
            lista.append(num)
        except ValueError:
            print("Errore: inserire un numero valido.")
    # return sum(lista)
    risultato = sum(lista)
    print("La somma dei numeri inseriti nella lista è: ", risultato)

def uscita_programma():
    conferma = input("Sei sicuro di voler uscire? (s/n): ").strip().lower()
    if conferma == 's':
        print("Programa terminato! Grazie per aver calcolato con noi.")
        return True
    else:
        print("Ritorno al menu principale.")
        return False

print("Benvenuti a tutti nel programma della calcolatrice!")
while True:
    print("""
    Seleziona un numero da 1 a 6 per eseguire i seguenti passaggi:
    - Per effettuare un'Addizione, seleziona 1;
    - Per effettuare una Sottrazione, seleziona 2;
    - Per effettuare una Moltiplicazione, seleziona 3;
    - Per effettuare una Divisione, seleziona 4;
    - Per effettuare un Calcolo Esponenziale, seleziona 5;
    - Per effettuare una Radice Quadrata, seleziona 6;
    - Per effettuare una somma di più numeri in una lista, seleziona 7;
    - Per uscire dal programma puoi digitare 'E';
    """)

    scelta = input("Inserisci il numero scelto: ")

    if scelta == "1":
        addizione()

    elif scelta == "2":
        sottrazione()

    elif scelta == "3":
        multipliczione()

    elif scelta == "4":
        divisione()

    elif scelta == "5":
        esponenza()

    elif scelta == "6":
        radiceQ()

    elif scelta == "7":
        somma_lista()

    elif scelta.upper() == "E":
        if uscita_programma():
            break
    #         oppure possiamo utilizzare il codice qui sotto senza metodo
    #     print("Programa terminato! Grazie per aver calcolato con noi.")
    #     break
    # else:
    #     print("Scelta non valida. Inserisci un numero richiesto oppure digita ESC per chiudere il programma.")