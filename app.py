const heartCount = 50;
const body = document.body;

for (let i = 0; i < heartCount; i++) {
    let heart = document.createElement("div");
    heart.innerHTML = "❤️";
    heart.style.position = "fixed";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.top = "-2vh";
    heart.style.fontSize = (Math.random() * 20 + 20) + "px";
    heart.style.animation = `fall ${Math.random() * 3 + 2}s linear forwards`;
    body.appendChild(heart);
}

let style = document.createElement("style");
style.innerHTML = `
@keyframes fall {
    to {
        transform: translateY(100vh);
        opacity: 0;
    }
}
`;
document.head.appendChild(style);
