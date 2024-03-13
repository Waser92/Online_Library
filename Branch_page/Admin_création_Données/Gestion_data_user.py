import json
import os

class GestionData:

    def save_data(self, data):
        # Chemin du fichier JSON
        file_path = 'C:/Data/MainData.json'

        # Charger les données existantes (si le fichier existe)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Mettre à jour les données existantes avec les nouvelles données
        existing_data.update(data)

        # Écrire les données mises à jour dans le fichier JSON
        with open(file_path, 'w') as file:
            json.dump(existing_data, file)

        # Utiliser le site comme clé principale
        nom_oeuvre = data.get('entry_nom_oeuvre')

        # Vérifier si 'site' est présent dans les données
        if nom_oeuvre is not None:
            # Ajouter ou mettre à jour les données pour le site spécifié
            existing_data[nom_oeuvre] = {
                "nom_oeuvre": data.get("entry_nom_oeuvre"),
                "email": data.get("entry_email"),
                "identifiant": data.get("entry_identifiant"),
                "mot_de_passe": data.get("entry_password")
            }
        else:
            pass

        # Écrire les données dans le fichier
        with open(self.user_data_filename, 'w') as file:
           json.dump(existing_data, file, indent=4)