import streamlit as st

st.set_page_config(page_title="¿Me perdonas?", page_icon="🙏")

st.title("¿Me perdonas?")

# Usamos el estado de sesión para rastrear si el botón "No" ya fue presionado
if "mostrar_no" not in st.session_state:
    st.session_state.mostrar_no = True

col1, col2 = st.columns(2)

with col1:
    if st.button("Sí"):
        st.success("💖 ¡Gracias por perdonarme!")
        st.session_state.mostrar_no = True  # restauramos el estado por si acaso

with col2:
    if st.session_state.mostrar_no:
        if st.button("No"):
            st.session_state.mostrar_no = False
