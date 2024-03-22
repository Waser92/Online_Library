from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os


class MyWindow_connection:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.config(background='#030720')
        self.nom_oeuvre_var = StringVar()
        self.Description_var = StringVar()
        self.Chemin_var = StringVar()

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
        label_title = Label(self.frame_top, text="\n Création d'une nouvelle page\n ", font=("Courier", 35), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Entrez les données \n qui seront affichées", font=("Courier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()

    def entry_fields(self):
        self.entry_nom_oeuvre = Entry(self.frame_center, textvariable=self.nom_oeuvre_var, font=("Courier", 15))
        self.entry_Description = Entry(self.frame_center, textvariable=self.Description_var, font=("Courier", 15))  
        self.entry_Chemin = Entry(self.frame_center, textvariable=self.Chemin_var, font=("Courier", 15))  

        self.entry_nom_oeuvre.insert(0, "Nom de l'oeuvre")
        self.entry_nom_oeuvre.config(fg='grey')

        self.entry_Description.insert(0, "Description")
        self.entry_Description.config(fg='grey')

        self.entry_Chemin.insert(0, "Chemin du fichier")
        self.entry_Chemin.config(fg='grey')

        # Ajout des gestionnaires d'événements de clic
        self.entry_nom_oeuvre.bind("<FocusIn>", self.clear_entry)
        self.entry_nom_oeuvre.bind("<FocusOut>", self.restore_default_text)

        self.entry_Description.bind("<FocusIn>", self.clear_entry)
        self.entry_Description.bind("<FocusOut>", self.restore_default_text)

        self.entry_Chemin.bind("<FocusIn>", self.clear_entry)
        self.entry_Chemin.bind("<FocusOut>", self.restore_default_text)

        self.entry_nom_oeuvre.pack()
        self.entry_Description.pack()
        self.entry_Chemin.pack()

    def create_buttons(self):
        style = ttk.Style()
        style.configure("TButton", padding=(20, 10))

        bouton_valider = ttk.Button(self.frame_center, text="Valider", command=lambda: self.save_data(self.nom_oeuvre_var.get(), self.Description_var.get(), self.Chemin_var.get()))
        bouton_valider.pack(pady=10)


    # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    def clear_entry(self, event):
        widget = event.widget
        if widget == self.entry_nom_oeuvre:
            initial_text = "Nom de l'oeuvre" 
        elif widget == self.entry_Description:  # Correction ici
            initial_text = "Description"  # Correction ici
        else:
            initial_text = "Chemin du fichier"  # Correction ici

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    def restore_default_text(self, event):
        widget = event.widget
        if widget == self.entry_nom_oeuvre:
            initial_text = "Nom de l'oeuvre" 
        elif widget == self.entry_Description:  # Correction ici
            initial_text = "Description"  # Correction ici
        else:
            initial_text = "Chemin du fichier"  # Correction ici
            
        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

    # Méthode pour enregistrer les données saisies
    def save_data(self, nom_oeuvre, description, chemin):
        # Chemin vers le fichier JSON
        chemin_fichier = 'page_principale\Data.json'

        # Charger les données existantes (si le fichier existe)
        if os.path.exists(chemin_fichier):
            with open(chemin_fichier, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Utiliser le nom de l'oeuvre comme clé principale
        if nom_oeuvre is not None and nom_oeuvre.strip() != "":
            # Ajouter ou mettre à jour les données pour l'oeuvre spécifiée
            existing_data[nom_oeuvre] = {
                "nom_oeuvre": nom_oeuvre,
                "description": description,
                "chemin": chemin
            }

            # Écrire les données dans le fichier JSON
            with open(chemin_fichier, 'w') as file:
                json.dump(existing_data, file, indent=4)

            messagebox.showinfo("Sauvegarde", "Les données ont été enregistrées avec succès.")
        else:
            messagebox.showerror("Erreur", "Le nom de l'oeuvre est invalide.")

        

# Display
app = MyWindow_connection()
app.window.mainloop()