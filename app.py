import streamlit as st
import requests
from datetime import date

st.write("# GHG Clan Zertifikat")
st.write("Bitte füllen Sie alles aus.")
n=st.text_input("Ihr Vorname und Nachname:")
b=st.date_input("Ihr Geburstsdatum:")
p=st.text_input("Welche positive Eigenschaft bringen Sie dem GHG-Clan mit sich?")
w=st.text_input("Warum möchten Sie in den legendären GHG-Clan?")
ghg=st.radio("Für was meinen Sie steht GHG?",
options=["German Hunger Games","Geh nach Hause","787"])

if st.button("Abschicken"):
    url = "http://localhost/save.php"
    payload={
        "Name": n,
        "Geburtstag": b.isoformat(),
        "Positiv": p,
        "Warum": w,
        "GHG": ghg
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        st.write("# Fertig!")
        st.write("Vielen Dank für die Bewerbung, wir werden sie in Kürze bearbeiten.")
        st.balloons()
    else:
        st.write("# Fehler")
        st.write("Die Server zum Abschicken sind leider nicht erreichbar!")
        st.write("Bitte versuchen sie es später erneut.")
