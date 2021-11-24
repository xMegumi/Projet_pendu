import random
from time import sleep

from functions import *
from graph import *

# Création du choix que l'utilisateur doit faire
choice = ""
while choice != "joueur" and choice != "arbitre":
    choice = input("Voulez-vous être le joueur ou l'arbitre ? [joueur/arbitre] ").lower()


if choice == 'joueur':
    # Génère un mot aléatoire à partir du fichier txt "mots_francais_sans_accents"
    random_word = random.choice(open("mots_francais_sans_accents.txt","r").readlines())

    # Transforme le mot en majuscule 
    word = random_word.upper()

    # Transforme le mot en liste puis retire "\n" de la fin.'
    word = list(word)
    word.remove("\n")
else:
    # Demande un mot, retire ses accents puis le met en majuscule
    word = str(input("Veuillez entrer un mot : "))
    word = remove_accents(word).upper()
    word = list(word)


# Création des variables utiles au programme.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
erreur = 0
affichage = []
lettre_memoire = []

# Fabrication de l'affichage les caractères deviennent des "*" et les espaces deviennent des "-".
for i in range(len(word)):
    if word[i] == " " or word[i] == "-":
        word[i] = "-"
        affichage.append("-")
    else:
        affichage.append("*")


# Boucle principale du programme.
print(*affichage)
while erreur < 8 and affichage != word:
    if choice == 'joueur':
        lettre = str(input("Entrez une lettre : ")).upper()
    else:
        sleep(1.5)
        lettre = random.choice(letters).upper()
        letters.remove(lettre.lower())

    # Vérifie si l'utilisateur ne donne qu'une seule lettre.
    if len(lettre) != 1:
            print("Entrer qu'une seule lettre.")

    # Vérifie si la lettre dans la mémoire.        
    elif lettre in lettre_memoire:
            print("Cette lettre a déjà été utilisée.")

    # Vérifie si la lettre est dans le mot 
    elif lettre in word:
        lettre_memoire.append(lettre)
        
        # Utilise le return de la fonction 'indices" pour l'affichage.
        for i in indices(lettre, word):
            affichage[i] = lettre

            if choice == 'joueur':
                print(*affichage)
            else:
                print("L'ordinateur a trouvé une lettre : ", lettre)
                print(*affichage)
        
    else:

        lettre_memoire.append(lettre)
        erreur += 1
        print(graph[erreur-1])

        if choice == 'joueur':
            print(*affichage)
        else:
            print("L'ordinateur s'est trompé. Lettre :", lettre)
            print(*affichage)


# Affiche la victoire ou la défaite.
if choice == 'joueur':
    if erreur == 8:
        print("Vous avez perdu, le mot était :",*word)
    else:
        print("Vous avez gagner")
else:
    if erreur == 8:
        print("Vous avez gagner, l'ordinateur a perdu !")
    else:
        print("Bravo ! L'ordinateur a perdu.")
