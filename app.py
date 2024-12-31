from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps  # Pour la sérialisation correcte des ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.cve_database
cve_collection = db.cves

@app.route('/cves', methods=['POST'])
def add_cve():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Simuler l'ajout de CVE et répondre avec un message
    cve_collection.insert_one(data)
    return jsonify({"message": "CVE added!"}), 201

@app.route('/seecves', methods=['GET'])
def get_cves():
    cves = list(cve_collection.find())  # Récupérer toutes les CVEs
    
    # Créer une version formatée de chaque CVE
    formatted_cves = []
    for cve in cves:
        formatted_cve = {
            "id": str(cve["_id"]),  # Convertir ObjectId en chaîne de caractères
            "description": cve.get("description", "No description available"),
            "severity": cve.get("severity", "Unknown")
        }
        formatted_cves.append(formatted_cve)

    # Retourner les données formatées en JSON
    return jsonify(formatted_cves)

if __name__ == "__main__":
    app.run(debug=True)
