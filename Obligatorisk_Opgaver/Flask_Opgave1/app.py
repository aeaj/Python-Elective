#Byg en simpel REST API med Flask
'''
1. Importer flask og håndtere HTTP-request 
som GET, POST, PUT, OG PATCH

2. Opret en liste med members som kan benytte sig af CRUD funktionerne

3. Lav routes til CRUD-funktionerne

4. Gør brug af HTTP-requests i form af POSTMAN ifbm. 
oprettelse af nye medlemmer og teste om de er oprettet
korrekt'''

#Validering og fejl-håndtering
'''
1. API'et skal returnerer korrekte
http-statuskoder (200 succes, 201 Created, 400 Bad request,
404 Not found, osv...)

2. Vis fejl, hvis request mangler data eller 
ID ikke findes'''

#SQLite-database
'''
1. Importer sqlite3 og opret en database(members.db)

2. Lav en tabel i databasen med attributterne

3. Gem og hent data fra databasen i stedet for listen'''

from flask import Flask, request, jsonify

#Opretter Flask applikation
app = Flask(__name__) 

# Database: Liste af medlemmer i form af dictionary[]
members = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "birth_date": "1990-01-01",
        "gender": "Male",
        "email": "john@example.com",
        "phonenumber": "12345678",
        "address": "Main Street 1",
        "nationality": "Danish",
        "active": True,
        "github_username": "johndoe"
    }
]

# Gemmer en liste over nødvendige felter i en variabel
# for senere brug 

REQUIRED_FIELDS = [
    "first_name", "last_name", "birth_date", "gender", "email",
    "phonenumber", "address", "nationality", "active", "github_username"
]

#Definerer en GET-route (C, GET /api/members), hvor Flask returnerer
#hele member-listen som JSON.
#Husk at ændre tilføje den ny rute til den oprindelig URL adresse
#F.eks. http://127.0.0.1:5000/api/members'''

# POST tilføjer nye medlemmer til listen: R, POSt /api/members
# Vi modtager data fra POSTMAN/Klienten som JSON
# API'et returnerer det nye medlem og en statuskode 201 (Created)'''
# Begge HTTP-metoder i samme funktion for bedre læsebarhed
@app.route('/api/members', methods=['GET'])
def get_members():
    return jsonify(members), 200
    
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    return jsonify(member if member else {"error": "Member not found"}), 200 if member else 404
    
@app.route('/api/members', methods=['POST'])
def create_members():
        data = request.get_json()
        
        # Validér at alle nødvendige felter er med
        missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400  # 400 Bad Request
        
        # Opret nyt medlem med unikt ID
        new_member = {
            "id": members[-1]["id"] + 1 if members else 1,  # Automatisk ID
            **data  # Tilføjer alle felterne fra request-data
        }

        members.append(new_member)  # Tilføj til listen
        return jsonify(new_member), 201  # 201 Created

@app.route('/api/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    member = next((m for m in members if m["id"] == member_id), None)

    if not member:
        return jsonify({"error": "Member not found"}), 404

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Opdater medlemmet i listen korrekt
    for i, m in enumerate(members):
        if m["id"] == member_id:
            members[i].update(data)
            return jsonify(members[i]), 200

    return jsonify({"error": "Something went wrong"}), 500  # Fail-safe

@app.route('/api/members/<int:member_id>', methods=['DELETE'])
def delete_members(member_id):
        global members
        members = [m for m in members if m["id"] != member_id]
        return jsonify({"message": f"Member with ID {member_id} deleted"}), 200 #Succes request

# Starter Flask-serveren, 
# hvis scriptet køres i temrinalen ved 'python app.py'
# Sørger for at kører scriptet i den rette mappe
# hvor filen befinder sig i''' 

if __name__ == '__main__':
    app.run(debug=True)

#Kør python app.py i terminalen og åben URL adressen 
#Eller søge manuelt efter den i ny browser
#F.eks. http://127.0.0.1:5000/api/members