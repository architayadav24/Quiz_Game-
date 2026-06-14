let questions = [
    {
        question: "What is the capital of India?",
        options: ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        answer: "Delhi"
    },
    {
        question: "Who developed Python?",
        options: ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"],
        answer: "Guido van Rossum"
    },
    {
        question: "Which is a Python framework?",
        options: ["Django", "React", "Laravel", "Spring"],
        answer: "Django"
    },
    {
        question: "What keyword is used to define function in Python?",
        options: ["func", "def", "function", "define"],
        answer: "def"
    },
    {
        question: "Which language is used to create the structure of a web page?",
        options: ["java", "html", "python", "c++"],
        answer: "html"
    },
    {
        question: "which HTML tag is used for a line break?",
        options: ["p", "br", "hr", "lb"],
        answer: "br"
    },
    {
        question: "Which HTML tag is used to create a paragraph?",
        options: ["p", "br", "hr", "lb"],
        answer: "p"
    },
    {
        question: "What is the file extension for a JavaScript file?",
        options: ["js", "java", "py", "cpp"],
        answer: "js"
    },
    {
        question: "How many chambers does the human heart have?",
        options: ["2", "4", "6", "8"],
        answer: "4"
    },
    {
        question: "How many chambers does the human heart have?",
        options: ["2", "4", "6", "8"],
        answer: "4"
    },
    {
        question: "Which part of the body contains the femur bone?",
        options: ["Arm", "Leg", "Head", "Torso"],
        answer: "Leg"
    },
    {
        question: "भारत में कुल कितने राज्य हैं?",
        options: ["28", "29", "30", "31"],
        answer: "28"
    },
    {
        question: "एशिया विश्व का सबसे बड़ा महाद्वीप है?",
        options: ["एशिया", "अफ्रीका", "यूरोप", "ऑस्ट्रेलिया"],
        answer: "एशिया"
    },
    {
        
        question: "भारत का राष्ट्रीय खेल कौन सा है?",
        options: ["हॉकी", "क्रिकेट", "बैडमिन्टन", "थॉवल"],
        answer: "हॉकी"
    },
    {
        question: "विश्व का सबसे बड़ा महासागर कौन सा है?",
        options: ["प्रशांत महासागर", "अटलांटिक महासागर", "हिमालय महासागर", "आर्कटिक महासागर"],
        answer: "प्रशांत महासागर"
    }

];

let current = 0;
let score = 0;
let selectedAnswer = "";

function loadQuestion() {
    let q = questions[current];

    document.getElementById("question").innerText = q.question;

    let optionsDiv = document.getElementById("options");
    optionsDiv.innerHTML = "";

    q.options.forEach(opt => {
        let btn = document.createElement("div");
        btn.classList.add("option");
        btn.innerText = opt;

        btn.onclick = () => {
            selectedAnswer = opt;
            document.querySelectorAll(".option").forEach(b => b.style.background = "#f1f1f1");
            btn.style.background = "#c8f7c5";
        };

        optionsDiv.appendChild(btn);
    });
}

function nextQuestion() {
    if (selectedAnswer === questions[current].answer) {
        score++;
    }

    current++;

    selectedAnswer = "";

    if (current < questions.length) {
        loadQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById("quiz-box").classList.add("hidden");
    document.getElementById("result-box").classList.remove("hidden");
    document.getElementById("score").innerText = `${score} / ${questions.length}`;
}

function restartQuiz() {
    current = 0;
    score = 0;
    selectedAnswer = "";

    document.getElementById("quiz-box").classList.remove("hidden");
    document.getElementById("result-box").classList.add("hidden");

    loadQuestion();
}

// start quiz
loadQuestion();