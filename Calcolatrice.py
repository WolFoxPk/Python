import tkinter as tk
from math import sqrt, exp
import re

# Funzione per gestire il click dei pulsanti
def click(tasto):
    if tasto == "=":
        try:
            # Gestione delle operazioni con la %
            espressione = display.get().replace("%", "/100")
            risultato = str(eval(espressione))
            display.delete(0, tk.END)
            display.insert(tk.END, risultato)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Errore")
    elif tasto == "C":
        display.delete(0, tk.END)
    elif tasto == "DEL":
        current = display.get()
        if current:
            display.delete(len(current)-1, tk.END)
    elif tasto == "√":
        try:
            numero = float(display.get())
            risultato = str(sqrt(numero))
            display.delete(0, tk.END)
            display.insert(tk.END, risultato)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Errore")
    elif tasto == "EXP":
        try:
            numero = float(display.get())
            risultato = str(exp(numero))
            display.delete(0, tk.END)
            display.insert(tk.END, risultato)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Errore")
    elif tasto == "+/-":
        current = display.get()
        if current:
            try:
                numero = float(current)
                numero = -numero
                display.delete(0, tk.END)
                display.insert(tk.END, str(numero))
            except:
                pass
    else:
        display.insert(tk.END, tasto)

# Creazione interfaccia
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

#cambia il colore dello sfondo
root.configure(bg="#dfe6e9")

#definiamo il calcolo percentuale
def converti_percentuali(expr):
    # Trova tutti i numeri seguiti da % e li converte in (numero/100)
    return re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expr)



# Campo di input/display
# display = tk.Entry(root, width=40, font=("Arial", 16), bg="#ffffff")
# display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
display = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Definizione dei tasti
tasti = [
    ['√', 'EXP', '%', 'C'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['DEL', '0','+/-', '+', '=']
]

# Creazione dei pulsanti
for i, riga in enumerate(tasti):
    for j, tasto in enumerate(riga):
        for j, tasto in enumerate(riga):
            if tasto in ['+', '-', '*', '/', '=', '√', 'EXP', '%']:
                bg = "#fab1a0"  # Colore operatori
            elif tasto == 'C':
                bg = "#d21f1b"  # Colore "C"
            elif tasto == 'DEL':
                bg = "#ff7677"
            elif tasto == '+/-':
                bg = '#5f9ea0'
            else:
                bg = "#dfe6e9"  # Colore numeri

            bottone = tk.Button(
                root,
                text=tasto,
                padx=20,
                pady=20,
                font=("Arial", 16),
                bg=bg,
                fg="black",
                activebackground="#cccccc",
                command=lambda t=tasto: click(t)
            )
            bottone.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)

# Rende i pulsanti adattabili alla finestra
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # solo 4 colonne
    root.grid_columnconfigure(i, weight=1)

# Avvia la finestra
root.mainloop()
