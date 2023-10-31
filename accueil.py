
from tkinter import Tk, Canvas, Button
import webbrowser
import subprocess

def demarrer_simulateur_click():
    # Ferme l'interface actuelle
    #fenetre.destroy()

    # Exécute le script de l'interface du simulateur
    subprocess.Popen(["python", "main_tk.py"])

    
# Reste du code...

# Fonctions pour gérer les clics sur les boutons
def sujet_challenge_click():
    # Spécifiez le chemin complet vers votre fichier PDF
    pdf_path = "sujet_tournoi.pdf"

    # Ouvre le fichier PDF avec le lecteur de PDF par défaut
    webbrowser.open(pdf_path)


# Création de la fenêtre
fenetre = Tk()
fenetre.geometry("719x550")
fenetre.title("GreenCarLoan")

# Canvas principal
canvas = Canvas(fenetre, bg="#FFFFFF", height=550, width=719)
canvas.pack()

# Bouton "Sujet du Challenge"
sujet_challenge_button = Button(fenetre, text="Sujet du Challenge", command=sujet_challenge_click)
sujet_challenge_button.place(x=35, y=406, width=245, height=65)

# Bouton "Démarrer simulateur"
demarrer_simulateur_button = Button(fenetre, text="Démarrer simulateur", command=demarrer_simulateur_click)
demarrer_simulateur_button.place(x=404, y=406, width=260, height=65)

# Lancement de la boucle principale
fenetre.mainloop()
from tkinter import Tk, Canvas, Button

# Fonctions pour gérer les clics sur les boutons
def sujet_challenge_click():
    print("Bouton 'Sujet du Challenge' cliqué")

def demarrer_simulateur_click():
    print("Bouton 'Démarrer simulateur' cliqué")

# Création de la fenêtre
fenetre = Tk()
fenetre.geometry("719x550")
fenetre.title("GreenCarLoan")

# Canvas principal
canvas = Canvas(fenetre, bg="#FFFFFF", height=550, width=719)
canvas.pack()

# Bouton "Sujet du Challenge"
sujet_challenge_button = Button(fenetre, text="Sujet du Challenge", command=sujet_challenge_click)
sujet_challenge_button.place(x=35, y=406, width=245, height=65)

# Bouton "Démarrer simulateur"
demarrer_simulateur_button = Button(fenetre, text="Démarrer simulateur", command=demarrer_simulateur_click)
demarrer_simulateur_button.place(x=404, y=406, width=260, height=65)

# Lancement de la boucle principale
fenetre.mainloop()
