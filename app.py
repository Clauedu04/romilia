import streamlit as st

st.set_page_config(page_title="Vuelve conmigo 💔", page_icon="💖")

st.title("💔 Quiero que vuelvas conmigo 💔")

st.write("Cada vez que presiones el botón, es una disculpa desde el fondo de mi corazón...")

if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("💖 Disculpa mi amor 💖"):
    st.session_state.contador += 1

for _ in range(st.session_state.contador):
    st.markdown("<h1 style='text-align: center; color: red;'>❤️</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Disculpa mi amor</h3>", unsafe_allow_html=True)
