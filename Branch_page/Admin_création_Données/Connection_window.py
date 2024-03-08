from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
import json
from Branch_page.Admin_création_Données.Gestion_data_user import GestionUserData
import subprocess
import os
#030720

class MyWindow_connection():

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.iconbitmap("")
        self.window.config(background='#030720')
        self.nom_utilisateur_var = StringVar()
        self.mot_de_passe_var = StringVar()

        # Nouvelle instance de GestionUserData avec le nom d'utilisateur actuel
        self.user_data_manager = GestionUserData(self.username)

        # Initialisation of components
        self.frame_top = Frame(self.window, bg='#030720')
        self.frame_center = Frame(self.window, bg='#030720')
        self.frame_bottom = Frame(self.window, bg='#030720')

        # Packaging
        self.frame_top.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_center.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)
        
        # Creation of components
        self.create_widgets()

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.entry_fields()
        self.create_buttons()

    def create_title(self):
        label_title = Label(self.frame_top, text="\n Création d'une nouvelle page\n ", font=("Courrier", 40), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Entrez les données qui seront affichés", font=("Courrier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()


    def entry_fields(self):
        # Ajout des champs de saisie (Entry)
        self.entry_nom_oeuvre = Entry(self.frame_center, textvariable=self.nom_utilisateur_var, font=("Courrier", 15))
        self.entry_Description = Entry(self.frame_center, textvariable=self.mot_de_passe_var, font=("Courrier", 15))
        self.entry_Chemin = Entry(self.frame_center, textvariable=self.mot_de_passe_var, font=("Courrier", 15))

        # Ajout du texte initial "Nom de l'oeuvre" en gris clair
        self.entry_nom_oeuvre.insert(0, "Nom de l'oeuvre")
        self.entry_nom_oeuvre.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout du texte initial "Description" en gris clair
        self.entry_Description.insert(0, "Description")
        self.entry_Description.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout du texte initial "Chemin du fichier" en gris clair
        self.entry_Chemin.insert(0, "Chemin du fichier")
        self.entry_Chemin.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout des gestionnaires d'événements de clic
        self.entry_nom_oeuvre.bind("<FocusIn>", self.clear_entry)
        self.entry_nom_oeuvre.bind("<FocusOut>", self.restore_default_text)

        self.entry_Description.bind("<FocusIn>", self.clear_entry)
        self.entry_Description.bind("<FocusOut>", self.restore_default_text)

        self.entry_Chemin.bind("<FocusIn>", self.clear_entry)
        self.entry_Chemin.bind("<FocusOut>", self.restore_default_text)


    def create_buttons(self):
        # Ajustez le style des boutons pour augmenter la taille
        style = ttk.Style()
        style.configure("TButton", padding=(20, 10))

        bouton_valider = ttk.Button(self.frame_center, text="Valider", command=self.authentifier_callback)
        bouton_valider.pack(pady=10)

        # Bouton Rechercher
        bouton_rechercher = tk.Button(self.search_window, text="Rechercher", command=self.rechercher_callback)
        bouton_rechercher.pack(pady=10)


    # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    def clear_entry(self, event):
        widget = event.widget
        initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    # Méthode pour restaurer le texte initial si le champ de saisie est vide
    def restore_default_text(self, event):
        widget = event.widget
        initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair
        def rechercher_callback(self):
        site_recherche = self.entry_site.get()
        data = self.user_data_manager.get_user_data_by_site(site_recherche)

        if data:
            messagebox.showinfo("Résultat de la Recherche", f"Informations trouvées pour le site '{site_recherche}':\n"
                                                             f"Identifiant: {data.get('identifiant', 'N/A')}\n"
                                                             f"Email: {data.get('email', 'N/A')}\n"
                                                             f"Mot de passe: {data.get('mot_de_passe', 'N/A')}")
        else:
            messagebox.showinfo("Résultat de la Recherche", f"Aucune information trouvée pour le site '{site_recherche}'.")

    
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


# Display
app = MyWindow_connection()
app.window.mainloop()





    

    

