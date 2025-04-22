import streamlit as st
import random

st.set_page_config(page_title="Vuelve Conmigo 💔", page_icon="❤️", layout="centered")

st.title("💖 Quiero que vuelvas conmigo 💖")
st.write("Cada vez que presiones el corazón, te pido perdón...")

if st.button("💗"):
    mensajes = [
        "Disculpa mi amor",
        "Perdóname, aún te amo",
        "Te extraño, regresa por favor",
        "No fue mi intención, perdóname",
        "Cada latido es un 'lo siento'",
    ]
    st.markdown(f"<h3 style='text-align: center; color: red;'>{random.choice(mensajes)}</h3>", unsafe_allow_html=True)
