import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Perdóname 💔", layout="centered")

st.markdown("""
    <style>
    @keyframes fall {
        0% { top: -50px; opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }
    .heart {
        position: fixed;
        top: -50px;
        font-size: 40px;
        animation: fall 3s linear infinite;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>💘 ¡Perdóname porfa! 💘</h1>", unsafe_allow_html=True)

# Botón en forma de corazón
if st.button("💖 Presiona si me perdonas 💖"):
    # Lluvia de corazones usando HTML + JS
    components.html("""
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
        "https://media.tenor.com/8Zg6rJ6MZTcAAAAM/puppy-dog-eyes.gif",
        "https://media.tenor.com/TK8Cjch43DYAAAAM/cute-dog.gif",
        "https://media.tenor.com/Q9X1YwKUoLgAAAAM/dog-cute.gif",
        "https://media.tenor.com/-x-0hB66VtoAAAAM/dog-puppy.gif"
    ]
    imagen = random.choice(perritos)
    st.image(imagen, caption="¿Cómo decirle que no? 😭", width=300)

    frases = [
        "😢 Mira su carita... ¿le vas a decir que no?",
        "🥺 Hasta el perrito está triste...",
        "🙏 Dale una oportunidad, por los perritos...",
        "🐶 ¡Si me perdonas te regalo uno así!"
    ]
    st.markdown(f"### {random.choice(frases)}")

else:
    st.markdown("### 👉 Presiona el botón si quieres ver algo tierno...")
