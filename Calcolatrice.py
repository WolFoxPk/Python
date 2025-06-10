import tkinter as tk

# creiamo la finestra
root = tk.Tk()
root.title("Calcolatrice")
root.geometry("450x600")

#cambia il colore dello sfondo
root.configure(bg="#dfe6e9")

# Funzione per gestire il click dei pulsanti
def click(tasto):
    if tasto == "=":
        try:
            risultato = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, risultato)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Errore")
    elif tasto == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, tasto)

# Campo di input/display
display = tk.Entry(root, width=40, font=("Arial", 16), bg="#ffffff")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definizione dei tasti
tasti = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Creazione dei pulsanti
for i, riga in enumerate(tasti):
    for j, tasto in enumerate(riga):
        for j, tasto in enumerate(riga):
            if tasto in ['+', '-', '*', '/', '=']:
                bg = "#fab1a0"  # Colore operatori
            elif tasto == 'C':
                bg = "#ff7675"  # Colore "C"
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
