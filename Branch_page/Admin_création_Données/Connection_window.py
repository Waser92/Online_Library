from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importation du module Gestion_data_user depuis le package
from Gestion_data_user import GestionUserData

class MyWindow_connection:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.config(background='#030720')
        self.nom_utilisateur_var = StringVar()
        self.mot_de_passe_var = StringVar()

        # Nouvelle instance de GestionUserData
        self.user_data_manager = GestionUserData()

        self.frame_top = Frame(self.window, bg='#030720')
        self.frame_center = Frame(self.window, bg='#030720')
        self.frame_bottom = Frame(self.window, bg='#030720')

        self.frame_top.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_center.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        self.create_widgets()

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.entry_fields()
        self.create_buttons()

    def create_title(self):
        label_title = Label(self.frame_top, text="\n Création d'une nouvelle page\n ", font=("Courier", 40), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Entrez les données qui seront affichées", font=("Courier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()

    def entry_fields(self):
        self.entry_nom_oeuvre = Entry(self.frame_center, textvariable=self.nom_utilisateur_var, font=("Courier", 15))
        self.entry_Description = Entry(self.frame_center, textvariable=self.mot_de_passe_var, font=("Courier", 15))
        self.entry_Chemin = Entry(self.frame_center, font=("Courier", 15))

        self.entry_nom_oeuvre.insert(0, "Nom de l'oeuvre")
        self.entry_nom_oeuvre.config(fg='grey')

        self.entry_Description.insert(0, "Description")
        self.entry_Description.config(fg='grey')

        self.entry_Chemin.insert(0, "Chemin du fichier")
        self.entry_Chemin.config(fg='grey')

    def create_buttons(self):
        style = ttk.Style()
        style.configure("TButton", padding=(20, 10))

        bouton_valider = ttk.Button(self.frame_center, text="Valider", command=self.valider_callback)
        bouton_valider.pack(pady=10)


    # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    def clear_entry(self, event):
        widget = event.widget
        initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    # Méthode pour restaurer le texte initial si le champ de saisie est vide
    # def restore_default_text(self, event):
    #     widget = event.widget
    #     initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

    #     if not widget.get():
    #         widget.insert(0, initial_text)
    #         widget.config(fg='grey')  # Changer la couleur du texte en gris clair

    #     def rechercher_callback(self):
    #         site_recherche = self.entry_site.get()
    #     data = self.user_data_manager.get_user_data_by_site(site_recherche)

    #     if data:
    #         messagebox.showinfo("Résultat de la Recherche", f"Informations trouvées pour le site '{site_recherche}':\n"
    #                                                          f"Identifiant: {data.get('identifiant', 'N/A')}\n"
    #                                                          f"Email: {data.get('email', 'N/A')}\n"
    #                                                          f"Mot de passe: {data.get('mot_de_passe', 'N/A')}")
    #     else:
    #         messagebox.showinfo("Résultat de la Recherche", f"Aucune information trouvée pour le site '{site_recherche}'.")

    
    # Méthode pour supprimer les données liées au site
    def supprimer_callback(self):
        site_supprimer = self.entry_site.get()

        if site_supprimer:
            # Appeler la nouvelle méthode pour supprimer les données liées au site
            success = self.user_data_manager.delete_user_data_by_site(site_supprimer)

            if success:
                messagebox.showinfo("Suppression réussie", f"Données pour le site '{site_supprimer}' supprimées avec succès.")
            else:
                messagebox.showinfo("Aucune correspondance", f"Aucune information trouvée pour le site '{site_supprimer}'.")
        else:
            messagebox.showinfo("Entrée vide", "Veuillez entrer un nom de site pour supprimer les données correspondantes.")

def valider_callback(self):
        # Récupérer les valeurs des champs de saisie
        nom_oeuvre = self.entry_nom_oeuvre.get()
        description = self.entry_Description.get()
        chemin = self.entry_Chemin.get()

        # Afficher les données récupérées
        messagebox.showinfo("Données", f"Nom de l'oeuvre: {nom_oeuvre}\nDescription: {description}\nChemin du fichier: {chemin}")


# Display
app = MyWindow_connection()
app.window.mainloop()