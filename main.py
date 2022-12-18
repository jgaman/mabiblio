#streamlit app for the project
from classes.classes import *
from classes.cred import *

import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path


st.set_page_config(page_title="Biblio", page_icon=":book:", layout="centered", initial_sidebar_state="auto")



# ----USER AUTHENTICATION----

names = [jean.nom, lucile.nom]
usernames = ["Jean", "lucile"]
passwords = [1234, 1234]
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as f:
    hashed_passwords = pickle.load(f)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"mabiblio", "abcdef", cookie_expiry_days=20)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username or password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status == True:
    authenticator.logout("Logout", "sidebar")


#----SIDE BAR & APP----

    if name == "Jean":
        name = jean
    elif name == "Lucile":
        name = lucile
    else:
        pass

    st.sidebar.title(f"{name}")


    with st.sidebar:
        st.image('https://media.istockphoto.com/id/1222800571/fr/vectoriel/illustration-plate-de-vecteur-de-pile-de-livres-manuel-ouvert.jpg?s=170667a&w=0&k=20&c=BnyVSCQvzTyfd17w6SKWcXol4wVVlr-sFeKAnOGFwAw=')
        st.title("Biblio 1.1 ")
        menu = st.radio("📚 Menu 📚", ["Accueil", "Afficher les livres de la Bu", "Emprunter un livre","Retourner un livre", "Rechercher un livre"])
        st.info("Cette application est une application de gestion de livres et de Bibliothèques!")

#-----ACCUEIL-----
    if menu == "Accueil":
        st.title(f" Bienvenue à la Bibliothèque de {Charpenne}")
        st.write("Que souhaitez-vous faire ?")
        st.write("Pour cela, utilisez le menu à gauche.")


#-----EMPRUNTER UN LIVRE-----
    if menu == "Emprunter un livre":
        st.title("📚 Emprunter un Livre 📚")
        st.write("Pour emprunter un livre, veuillez remplir le formulaire ci-dessous.")

        #afficher tous les titre des livres de la bibliothèque

        titre = [Charpenne.livres[i].titre for i in range(len(Charpenne.livres))]
        choice = st.selectbox("Choisissez un livre", titre)

        # définir choice comme objet livre
        choice = Charpenne.livres[titre.index(choice)]

        st.write(f"Vous avez choisi le livre {choice.titre}")
        clicked = st.button("Emprunter")

        if len(name.emprunts) <= 4:
            if clicked:
            #emprunter le livre

            #rajouter le livre à la liste des livres empruntés
                name.emprunter(Charpenne, choice)
                st.write("")

                st.write("")
                st.write(f"Vous avez emprunté {len(name.emprunts)} livre(s) au total.")
                st.write("Voici la liste de vos emprunts :")
                st.table(name.emprunts)
        else:
            st.error("😶‍🌫️ Vous avez déjà emprunté 5 livres.")

#-----RETOURNER UN LIVRE-----

    if menu == "Retourner un livre":
        #essayer sinon afficher une erreur
        try:
            st.title("📚 Retourner un Livre 📚")
            st.write("Pour retourner un livre, veuillez remplir le formulaire ci-dessous.")

            #afficher tous les livres de la bibliothèque
            titre = [name.emprunts[i].titre for i in range(len(name.emprunts))]
            choice = st.selectbox("Choisissez un livre", titre)

            # définir choice comme objet livre
            choice = name.emprunts[titre.index(choice)]

            st.write(f"Vous avez choisi le livre {choice.titre}")
            number = st.number_input("📚 Notez le livre de 1 à 5", min_value=1, max_value=5, step=1)

            clicked = st.button("Retourner")

            if clicked:
                #retourner le livre
                name.retourner(Charpenne, choice)
                st.write("")
                st.success(f"Vous avez retourné le livre {choice.titre} !")
                st.write("")
                st.write(f"Vous avez emprunté {len(name.emprunts)} livre(s) au total.")
                st.write("Voici la liste de vos emprunts :")
                st.table(name.emprunts)
                choice.note.append(number)

        except:
            st.error("🤐 Vous n'avez pas d'emprunts en cours. Empruntez un livre pour pouvoir le retourner.")

#---RECHERCHER UN LIVRE---


    if menu == "Rechercher un livre":

        titre = [Charpenne.livres[i].titre for i in range(len(Charpenne.livres))]
        st.title('Rechercher un livre 📚')
        search = st.text_input('Entrer le titre du livre:')

        if search:
            if search in titre:
                st.write(f"Le livre {search} est disponible à la bibliothèque de {Charpenne.nom}")
                st.write("Voici les informations du livre :")
                st.success(Charpenne.livres[titre.index(search)])
            else:
                st.error("😶‍🌫️ Ce livre n'existe pas dans la bibliothèque.")

    if menu == "Afficher les livres de la Bu":
        st.title("📚 Afficher les livres 📚")
        st.write("Voici la liste des livres de la bibliothèque de Charpenne: ")
        st.table(Charpenne.livres)
        st.success("Un 📖 vous plairait-il ?")


# ----END OF APP----
#test


