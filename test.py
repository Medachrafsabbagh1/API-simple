import requests

url = "http://127.0.0.1:5000/cves"
headers = {"Content-Type": "application/json"}

# Liste des CVEs à ajouter
cves_data = [
    {"id": "CVE-2023-1234", "description": "An example vulnerability.", "severity": "High"},
    {"id": "CVE-2023-5678", "description": "Another example vulnerability.", "severity": "Medium"},
    {"id": "CVE-2023-9101", "description": "Yet another vulnerability example.", "severity": "Low"}
]

# Boucle pour envoyer chaque CVE
for cve in cves_data:
    response = requests.post(url, json=cve, headers=headers)
    
    # Afficher la réponse brute
    print(f"Response Text for {cve['id']}: {response.text}")
    
    # Si la réponse est correcte, afficher la réponse JSON
    if response.status_code == 201:
        print(f"CVE {cve['id']} added successfully!")
    else:
        print(f"Failed to add CVE {cve['id']}, Status Code: {response.status_code}")
