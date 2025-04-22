if si:
    st.success("¡Sabía que me perdonarías! 💕")
    
    corazones_js = """
    <html>
    <head>
    <style>
    @keyframes fall {
        to {
            transform: translateY(100vh);
            opacity: 0;
        }
    }
    .heart {
        position: fixed;
        animation: fall linear forwards;
        z-index: 9999;
    }
    </style>
    </head>
    <body>
    <script>
    const heartCount = 50;
    for (let i = 0; i < heartCount; i++) {
        let heart = document.createElement("div");
        heart.className = "heart";
        heart.innerHTML = "❤️";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.top = "-2vh";
        heart.style.fontSize = (Math.random() * 20 + 20) + "px";
        heart.style.animationDuration = (Math.random() * 3 + 2) + "s";
        document.body.appendChild(heart);
    }
    </script>
    </body>
    </html>
    """

    components.html(corazones_js, height=600)

