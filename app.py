import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="¿Me perdonas?", layout="centered")

st.title("¿Me perdonas? 😢")

col1, col2 = st.columns(2)

with col1:
    si = st.button("💖 Sí")

with col2:
    no = st.button("💔 No")

if si:
    st.success("¡Sabía que me perdonarías! 💕")
    with open("assets/corazones.js") as f:
        js_code = f.read()
    components.html(
        f"""
        <html>
        <body>
        <script>
        {js_code}
        </script>
        </body>
        </html>
        """,
        height=600
    )
elif no:
    st.info("Ok... espero tu perdón algún día 😔")
