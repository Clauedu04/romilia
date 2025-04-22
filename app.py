import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Perdóname 💔", layout="centered")

st.markdown("<h1 style='text-align: center;'>💘 ¡Perdóname porfa! 💘</h1>", unsafe_allow_html=True)

# Botón en forma de corazón
if st.button("💖 Presiona si me perdonas 💖"):
    # Lluvia de corazones usando HTML
    components.html("""
    <style>
        body {
            background: transparent;
        }
        .heart {
            position: fixed;
            top: -50px;
            font-size: 40px;
            animation: fall 3s linear infinite;
        }
        @keyframes fall {
            0% { top: -50px; opacity: 1; }
            100% { top: 100%; opacity: 0; }
        }
    </style>
    <script>
        function createHearts() {
            for (let i = 0; i < 30; i++) {
                let heart = document.createElement("div");
                heart.classList.add("heart");
                heart.style.left = Math.random() * 100 + "vw";
                heart.style.animationDuration = 2 + Math.random() * 3 + "s";
                heart.innerHTML = "❤️";
                document.body.appendChild(heart);
            }
        }
        createHearts();
    </script>
    """, height=0)

    # Imagen de perrito aleatorio
    perritos = [
        "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
        "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
        "https://media.giphy.com/media/6uMqzcbWRhoT6/giphy.gif",
        "https://media.giphy.com/media/1BcfiGlOGXzQk/giphy.gif"
    ]
    st.image(random.choice(perritos), width=300)
    st.markdown("### 😢 Mira su carita... ¿le vas a decir que no?")

else:
    st.markdown("### 👉 Presiona el botón si quieres ver algo tierno...")

