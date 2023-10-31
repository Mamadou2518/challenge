import tkinter as tk
import json

# Fonction pour calculer le taux d'emprunt en fonction des critères
def calculer_taux_emprunt():
    type_vehicule = type_vehicule_var.get()
    energie = energie_var.get()
    kilometrage = kilometrage_var.get()
    annee = annee_var.get()
    passagers = passagers_var.get()

    score_vehicule = (
        donnees_voitures["type_vehicules"][type_vehicule]["Note Eco"] +
        donnees_voitures["energies"][energie]["Note Eco"] +
        donnees_voitures["kilometrage"][kilometrage]["Note Eco"] +
        donnees_voitures["annee"][annee]["Note Eco"]
    )

    # Obtention du taux d'emprunt en fonction du score véhicule
    taux_emprunt = None
    for plage, taux_data in donnees_bancaires["taux_emprunt"].items():
        debut, fin = map(int, plage.split('-'))
        if debut <= score_vehicule <= fin:
            taux_emprunt = float(taux_data["Taux emprunt"][:-1]) / 100  # Convertir en valeur numérique
            break

    if taux_emprunt is None:
        print("Les données de taux d'emprunt ne sont pas disponibles pour ce score.")
        return None

    # Obtention du bonus/malus en fonction du nombre de passagers
    if passagers in donnees_bancaires["passagers"]:
        bonus_malus = float(donnees_bancaires["passagers"][passagers]["bonus/malus"][:-1]) / 100
    else:
        bonus_malus = 0.0  # Pas de bonus/malus si le nombre de passagers n'est pas trouvé

    # Calcul du taux d'emprunt final en appliquant le bonus/malus
    taux_emprunt_final = taux_emprunt * (1 + bonus_malus)

    # Calcul du taux d'emprunt (votre fonction de calcul ici)
    taux_emprunt = taux_emprunt_final 

    # Affichage du résultat
    resultat_label.config(text=f"Le taux d'emprunt est de {taux_emprunt:.2%}")

# Créez une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Simulateur de prêt pour l'achat d'une voiture")

# Chargez les données à partir des fichiers JSON
with open('donnees_voitures.json', 'r') as fichier_voitures:
    donnees_voitures = json.load(fichier_voitures)

with open('donnees_bancaires.json', 'r') as fichier_bancaires:
    donnees_bancaires = json.load(fichier_bancaires)

# Créez des libellés, des menus déroulants et un bouton dans la fenêtre
type_vehicule_label = tk.Label(fenetre, text="Type de véhicule :")
type_vehicule_label.grid(row=0, column=0)
type_vehicule_var = tk.StringVar()
type_vehicule_var.set(list(donnees_voitures["type_vehicules"].keys())[0])
type_vehicule_menu = tk.OptionMenu(fenetre, type_vehicule_var, *donnees_voitures["type_vehicules"].keys())
type_vehicule_menu.grid(row=0, column=1)

energie_label = tk.Label(fenetre, text="Énergie :")
energie_label.grid(row=1, column=0)
energie_var = tk.StringVar()
energie_var.set(list(donnees_voitures["energies"].keys())[0])
energie_menu = tk.OptionMenu(fenetre, energie_var, *donnees_voitures["energies"].keys())
energie_menu.grid(row=1, column=1)

kilometrage_label = tk.Label(fenetre, text="Kilométrage :")
kilometrage_label.grid(row=2, column=0)
kilometrage_var = tk.StringVar()
kilometrage_var.set(list(donnees_voitures["kilometrage"].keys())[0])
kilometrage_menu = tk.OptionMenu(fenetre, kilometrage_var, *donnees_voitures["kilometrage"].keys())
kilometrage_menu.grid(row=2, column=1)

annee_label = tk.Label(fenetre, text="Année :")
annee_label.grid(row=3, column=0)
annee_var = tk.StringVar()
annee_var.set(list(donnees_voitures["annee"].keys())[0])
annee_menu = tk.OptionMenu(fenetre, annee_var, *donnees_voitures["annee"].keys())
annee_menu.grid(row=3, column=1)

passagers_label = tk.Label(fenetre, text="Nombre de passagers :")
passagers_label.grid(row=4, column=0)
passagers_var = tk.StringVar()
passagers_var.set(list(donnees_bancaires["passagers"].keys())[0])
passagers_menu = tk.OptionMenu(fenetre, passagers_var, *donnees_bancaires["passagers"].keys())
passagers_menu.grid(row=4, column=1)

calculer_button = tk.Button(fenetre, text="Calculer le taux d'emprunt", command=calculer_taux_emprunt)
calculer_button.grid(row=5, column=0, columnspan=2)

resultat_label = tk.Label(fenetre, text="")
resultat_label.grid(row=6, column=0, columnspan=2)

# Lancez la boucle principale de l'interface utilisateur
fenetre.mainloop()
