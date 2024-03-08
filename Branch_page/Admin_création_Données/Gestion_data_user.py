import json
import os

class GestionData:

    def save_data(self, data):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(Data.json):
            with open(, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

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

    def load_user_data(self):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)

            # Triez les données par le site
            sorted_data = sorted(user_data.items(), key=lambda x: x[0])

            return [data[1] for data in sorted_data]
        else:
            return []
        
    def get_user_data_by_site(self, site):
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)
            return user_data.get(site, {})
        else:
            return {}
        
    def delete_user_data_by_site(self, site):
        try:
            # Charger les données existantes
            user_data = self.load_user_data()

            # Vérifier si le site existe dans les données
            if site in user_data:
                # Supprimer les données liées au site
                del user_data[site]

                # Enregistrer les données mises à jour
                self.save_user_data(user_data)
                return True
            else:
                # Le site n'existe pas dans les données
                return False
        except Exception as e:
            return False