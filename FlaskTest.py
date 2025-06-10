from flask import Flask, request, jsonify

app = Flask(__name__)

# Variabile lista per salvare gli utenti
users = []

@app.route('/home/<name>')
def home(name):
    return f"Welcome to {name} HomePage!"

@app.post('/createUser')
def createUser():
    try:
        # Debug: stampa informazioni sulla richiesta
        # print("Content-Type:", request.content_type)
        # print("Raw data:", request.get_data())

        dati_User = request.json  # Ottiene i dati JSON dalla richiesta
        # print("Parsed JSON:", dati_User)

        if not dati_User:  # Verifica che ci siano dati
            return jsonify({"Errore": "Nessun dato fornito"}), 400

        # Verifica che ci sia almeno il campo nome (usando 'nome' come nel JSON)
        if 'nome' not in dati_User:
            return jsonify({"Errore": "Il campo 'nome' è obbligatorio"}), 400

        users.append(dati_User)  # Aggiungi l'utente alla lista

        return jsonify({
            "messaggio": "User created successfully!",
            "User": dati_User
        }), 201

    except Exception as e:
        return jsonify({"Errore": str(e)}), 500

# RITORNA TUTTI GLI UTENTI SALVATI NELLA VARIABILE, NON SOLO UNO
@app.route('/getUsers')
def getUsers():
    return jsonify({
        "users": users,
        "total": len(users)
    })

# RITORNA TUTTI GLI UTENTI SALVATI NELLA VARIABILE con quel nome
@app.get('/getUser/<name>')
def getUser(name):
    user_found = [user for user in users if user.get('nome', '').lower() == name.lower()] # Trova tutti gli utenti con quel nome

    if user_found:
        return jsonify({
            "users": user_found,
            "total": len(user_found),
        })
    else:
        return jsonify({
            "ERROR": f"User not found with name: '{name}'",
            "users": []
        }), 404

if __name__ == '__main__':
    app.run(debug=True)