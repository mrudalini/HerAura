const quotes = [
    "You are doing your best 🌷",
    "Rest is part of growth 💛",
    "Be gentle with yourself 🌸",
    "Your body listens to your care ✨"
];

document.getElementById("quote").innerText =
    quotes[Math.floor(Math.random() * quotes.length)];

function savePeriod() {
    const date = document.getElementById("period").value;
    localStorage.setItem("period", date);
    document.getElementById("phase").innerText =
        "Your cycle is noted 🌸 Take gentle care today.";
}

function saveFood() {
    localStorage.setItem("food", document.getElementById("food").value);
    alert("Food routine saved 🍽️");
}

function saveMood() {
    const mood = document.getElementById("mood").value;
    let tip = "Stay hydrated and eat balanced meals 💛";

    if (mood === "Low") tip = "Warm food and rest may help today 🌷";
    if (mood === "Tired") tip = "Iron-rich food can support energy 🌸";

    document.getElementById("tip").innerText = tip;
}

function saveJournal() {
    localStorage.setItem("journal", document.getElementById("journal").value);
    alert("Your feelings are safely saved 💕");
}