import streamlit_authenticator as stauth
import pickle
from pathlib import Path
from classes.classes import *

names = [jean, lucile]
usernames = [jean.username, lucile.username]
passwords = [jean.password, lucile.password]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as f:
    pickle.dump(hashed_passwords, f)


