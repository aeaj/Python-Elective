from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/get-user/<user_id>") #Path parameter for getting a value for user
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
        }
    
    extra = request.args.get("extra")
    
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)

'''Kører programmet i terminalen 
ved at skrive 'python api.py' som er filens navn'''

'''Efterølgende vil der opstå en advarselstegn,
    og du vil hermed få vist en url, som er din 
    oprettede root i en flask. Klik på den for at 
    tilgå data'''

#Http Metoder: 
# GET, Anmode om data fra en resource
# POST, Opret ressource
# PUT, Opdater ressource
# DELETE, Slette resource

