# Project UML BIBLIOTHEQUE
# Auteur: Jean-Luc GAMAN & Baptiste CARTIER
import datetime
import itertools # pour id auto-increment
import streamlit as st
import pandas as pd



class Livres:

    """La classe `Livres` est un schéma de création d'objets représentant un livre
    :param titre: titre du livre
    :type titre: str
    :param auteurs: nom de l'auteur
    :type auteurs: str
    :param edition: édition du livre
    :type edition: str
    :param date_enregistrement: date d'enregistrement du livre"""

    stars = ["👎", "✨", "✨✨", "✨✨✨", "✨✨✨✨", "✨✨✨✨✨"]
    id_obj = itertools.count(2)

    def __init__(self, titre: str, auteurs: str, edition: str, genre: str, note: list):

        self.idl = next(self.id_obj)
        self.titre = titre
        self.auteurs = auteurs
        self.edition = edition
        self.date_enregistrement = datetime.datetime.now()
        self.genre = genre
        self.note = note
        self.idbiblio = 0

    def __str__(self):
        return "📖 Titre: " + self.titre +" Son id est : "+ str(self.idl) + ", "+ "Auteur: " + self.auteurs + ", Genre: " + self.genre + ", Note du Public: " + str(Livres.stars[self.note])


class Bibliotheque:

        """La classe `Bibliotheque` est un schéma de création d'objets représentant une bibliothèque
        :param nom: Le nom de la bibliothèque
        :type nom: str
        :param adresse: L'adresse de la bibliothèque
        :type adresse: str
        :param livres: liste de livres
        :type livres: list
        """
        id_obj = itertools.count(1)

        def __init__(self, nom: str, adresse: str, livres: list, horraire: str):

            self.idb = next(self.id_obj)
            self.nom = nom
            self.adresse = adresse
            self.livres = livres
            self.horraire = horraire
            self.user = []

        def __str__(self):
            return "🏠 " + self.nom


        def afficher_livres(self):
            """
            La fonction afficher_livres affiche les livres de la bibliothèque.
            """
            print(f"📚 Les Livres de la Bibliothèque de {self.nom}:")
            for livre in self.livres:
                print(livre)


class Utilisateurs:

    """La classe `Utilisateurs` est un schéma de création d'objets représentant un utilisateur
        :param nom: Le nom de la personne
        :type nom: str
        :param date_naissance: date de naissance
        :type date_naissance: datetime
        :param statut: "admin" or "etudiant
        :type statut: str"""

    stars = ["👎", "✨", "✨✨", "✨✨✨", "✨✨✨✨", "✨✨✨✨✨"]  # pour les notes des livres

    id_obj = itertools.count(1)

    def __init__(self, nom: str, date_naissance: datetime, date_enregistrement: datetime, statut = "admin"):

        self.id = next(self.id_obj)  # unique id & auto-increment
        self.nom = nom
        self.date_naissance = date_naissance
        self.statut = statut
        self.date_enregistrement = date_enregistrement
        self.emprunts = []
        self.username = nom
        self.password = "1234"

    def __str__(self):
        return "🤓 Bienvenue: " + self.nom + " !" + " \n Vous êtes un " + self.statut

    def emprunter(self, bibliotheque: Bibliotheque, livre: Livres):
        """
        > La fonction `emprunter` prend en arguments un objet `Bibliotheque` et un objet `Livre` et ajoute l'objet `Livre` à
        la liste `emprunts` de l'objet `Bibliotheque`

        :param bibliotheque: Bibliotheque, livre: Livres
        :type bibliotheque: Bibliotheque
        :param livre: Livres
        :type livre: Livres
        """
        date = datetime.datetime.now()

        if livre in bibliotheque.livres:
            self.idbiblio = bibliotheque.idb
            self.emprunts.append(livre)
            bibliotheque.livres.remove(livre)
            st.success(f"📚 Merci! Le livre a été emprunté à la bibliothèque: {bibliotheque.nom}, le {date}")

        elif livre in self.emprunts:
            st.write("😁 Vous avez déjà emprunté ce livre !")

        elif len(self.emprunts) >= 5:
            st.write("😁 Vous avez déjà emprunté 5 livres !")

        else:
            st.write("😒 Le livre que vous chercher n'est pas disponible dans cette bibliothèque !")

    def retourner(self, bibliotheque: Bibliotheque, livre: Livres):
        """
        > La fonction `retourner` prend en paramètres un objet `Bibliotheque` et un objet `Livres` et supprime l'objet
        `Livres` de la liste `emprunts` de l'objet `Bibliotheque`

        :param bibliotheque: Bibliotheque, livre: Livres
        :type bibliotheque: Bibliotheque
        :param livre: Livres
        :type livre: Livres
        """
        if self.idbiblio == bibliotheque.idb:
            if livre in self.emprunts:
                self.emprunts.remove(livre)
                bibliotheque.livres.append(livre)


            else:
                print("😒 Vous n'avez pas emprunté ce livre dans cette bibliothèque !")

    def afficher_emprunts(self):
        """
        Il imprime un message indiquant le nombre de livres empruntés par l'utilisateur, puis imprime la liste des livres
        """

        print(f"🤓 {self.nom} a emprunté {len(self.emprunts)} livre(s), voici la liste:")
        for livre in self.emprunts:
            print(livre, end="\n")

    def user_info(self):
        """
        Cette fonction affiche les informations de l'utilisateur
        """
        if self.statut == "admin":
            return "Tu es un admin 🤖"
        else:
            return "Tu es un etudiant, Jeune Padawan 🤓"

    def noter(self, livre: Livres):
        """
        La fonction noter() prend un objet livre et demande à l'utilisateur de le noter

        :param livre: Livres
        :type livre: Livres
        """
        if livre in self.emprunts:

            try:
                note = int(input("Veuillez noter le livre sur 5: "))
                if note > 5:
                    note = int(input("La note doit être comprise entre 1 et 5: "))
                else:
                    livre.note = note
                    print(f"Merci! Vous avez noté le livre {livre.titre} avec {self.stars[note]}")

            except ValueError:
                print("Oops! Merci de ne rentrer que des nombres de 1 à 5. Réessayé...")
                note = int(input("Veuillez noter le livre sur 5: "))
                livre.note = note
        else:
            print("Vous n'avez pas emprunter ce livre!")

    def ajouter_livre(self, bibliotheque: Bibliotheque, livre: Livres):
        """
        > Si l'utilisateur est un admin et que le livre n'est pas déjà dans la bibliothèque, ajoutez le livre à la
        bibliothèque

        :param bibliotheque: Bibliotheque
        :type bibliotheque: Bibliotheque
        :param livre: Livres
        :type livre: Livres
        """
        if self.statut == "admin":
            if livre not in bibliotheque.livres:
                bibliotheque.livres.append(livre)
                print(f"{livre.titre} a été ajouté dans la collection de la bibliothèque: {bibliotheque.nom} !")
            else:
                st.write(f"🤐 {bibliotheque.nom} possède déjà {livre.titre} !")
        else:
            st.write("🛑 Vous n'avez pas le droit d'ajouter un livre à la bibliothèque !")

    def supprimer_livre(self, bibliotheque: Bibliotheque, livre: Livres):
        """
        > Si l'utilisateur est un administrateur et que le livre se trouve dans la bibliothèque, supprimez le livre de la
        bibliothèque

        :param bibliotheque: Bibliotheque
        :type bibliotheque: Bibliotheque
        :param livre: Livres
        :type livre: Livres
        """
        if self.statut == "admin":
            if livre in bibliotheque.livres:
                bibliotheque.livres.remove(livre)
                print(f"{livre.nom} a été supprimé de la collection de la bibliothèque: {bibliotheque.nom} !")
            else:
                print(f"{bibliotheque.nom} ne possède pas {livre.nom}!")
        else:
            print("🛑 Vous n'avez pas le droit de supprimer un livre de la bibliothèque !")

    def rechercher_livre(self, bibliotheque: Bibliotheque, titre: str):
        """
        > La fonction `rechercher_livre` prend en paramètres un objet `Bibliotheque` et un titre de livre et renvoie le
        livre s'il est trouvé

        :param bibliotheque: Bibliotheque
        :type bibliotheque: Bibliotheque
        :param titre: str
        :type titre: str
        :return: Livres
        :rtype: Livres
        """
        for livre in bibliotheque.livres:
            if titre in livre.titre:
                return livre
            else:
                print(f"🤔 {titre} n'est pas dans la collection de la bibliothèque: {bibliotheque.nom} !")




#seeds
guerre = Livres("La guerre des mondes", "H.G. Wells", "La fouintes" ,"fantastique", 4)
harry = Livres("Harry Potter", "J.K. Rowling", "Gallimard", "fantastique", 5)
hunger = Livres("Hunger Games", "Suzanne Collins", "Pocket", "fantastique", 3)
harry2 = Livres("Harry Potter 2", "J.K. Rowling", "Gallimard", "fantastique", 5)
dbz = Livres("Dragon Ball Z", "Akira Toriyama", "Pika", "manga", 3)
jordan = Livres("Le retour de la légende", "Michael Jordan", "Pocket", "sport", 4)
roi = Livres("Le roi lion", "Disney", "Disney", "dessin animé", 5)
tom = Livres("Tom Sawyer", "Mark Twain", "Pocket", "roman", 4)
nike = Livres("Nike", "Nike", "Nike", "sport", 5)
soleil = Livres("Le soleil des Scorta", "Jean M. Auel", "Pocket", "roman", 4)
naruto = Livres("Naruto", "Masashi Kishimoto", "Pika", "manga", 5)
harry3 = Livres("Harry Potter 3", "J.K. Rowling", "Gallimard", "fantastique", 5)
planet = Livres("La planète des singes", "Pierre Boulle", "Pocket", "fantastique", 4)
riot = Livres("Riot Games", "Riot Games", "Riot Games", "sport", 2)
alice = Livres("Alice au pays des merveilles", "Lewis Carroll", "Pocket", "roman", 5)

jean = Utilisateurs("Jean", "admin", datetime.date(1990, 1, 1))
lucile = Utilisateurs("Lucile", "etudiant", datetime.date(1996, 2, 1))
#instances de classes et testes

Charpenne = Bibliotheque("Charpenne", "23, Rue de la paix, Paris 75009", [guerre, harry, hunger, harry2, dbz, jordan, roi, tom, nike, soleil, naruto, harry3, planet, riot, alice], "9H-18H, fermé le dimanche")
