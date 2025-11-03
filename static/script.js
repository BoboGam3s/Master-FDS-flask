// Fichier : static/script.js

// --- Logique du Dark/Light Mode ---
function setupThemeToggle() {
    const toggleButtonNav = document.getElementById('theme-toggle'); // Bouton dans la nav (mobile)
    const toggleButtonDesktop = document.getElementById('theme-toggle-desktop'); // Bouton à l'extérieur (desktop)
    const body = document.body;
    
    // Fonction pour appliquer le thème
    function applyTheme(isDark) {
        if (isDark) {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
    }
    
    // 1. Appliquer le thème sauvegardé ou le thème système
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(savedTheme === 'dark' || (!savedTheme && prefersDark));

    // 2. Écouteur pour le bouton (synchronisation)
    function addToggleListener(button) {
        if (button) {
            button.addEventListener('click', () => {
                const isCurrentlyDark = body.classList.contains('dark-mode');
                applyTheme(!isCurrentlyDark);
            });
        }
    }
    
    addToggleListener(toggleButtonNav);
    addToggleListener(toggleButtonDesktop);
}

// --- Logique du Menu Mobile (Hamburger) ---
function setupMobileMenu() {
    const toggleButton = document.querySelector('.menu-toggle');
    const navList = document.getElementById('main-nav');

    if (toggleButton && navList) {
        toggleButton.addEventListener('click', () => {
            const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true' || false;
            
            toggleButton.setAttribute('aria-expanded', !isExpanded);
            
            // Utilise la classe CSS 'menu-show'
            navList.classList.toggle('menu-show');
        });
    }
}


document.addEventListener('DOMContentLoaded', () => {
    // Les données quizQuestions sont injectées dans index.html
    const quizForm = document.getElementById('quiz-form');
    const submitButton = document.getElementById('submit-button');
    const resultsSummary = document.getElementById('results-summary');

    // Configuration des fonctionnalités
    setupThemeToggle(); 
    setupMobileMenu(); 


    // --- Logique du Timer ---
    const timerElement = document.getElementById('timer');
    let timeLimitMinutes = 60; 
    let timeRemainingSeconds = timeLimitMinutes * 60;
    let timerInterval;

    function formatTime(totalSeconds) {
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    function startTimer() {
        if (!timerElement) return; 
        
        timerInterval = setInterval(() => {
            if (timeRemainingSeconds <= 0) {
                clearInterval(timerInterval);
                timerElement.textContent = "Temps écoulé !";
                if (quizForm) submitQuiz(new Event('submit')); 
            } else {
                timeRemainingSeconds--;
                timerElement.textContent = formatTime(timeRemainingSeconds);
            }
        }, 1000);
    }

    // Démarre le timer uniquement sur la page quiz
    if (quizForm) {
        startTimer();
    }


    // --- Logique de Soumission du Quiz ---
    function submitQuiz(event) {
        event.preventDefault(); 
        
        // S'assurer que les données existent (injectées dans index.html)
        if (typeof quizQuestions === 'undefined' || !quizQuestions) return;

        let correctCount = 0;
        const totalQuestions = quizQuestions.length;

        clearInterval(timerInterval);
        submitButton.disabled = true;

        quizQuestions.forEach(qData => {
            const container = document.querySelector(`.question-container[data-id="${qData.id}"]`);
            if (!container) return; 

            const questionName = `q_${qData.id}`;
            const selectedOption = document.querySelector(`input[name="${questionName}"]:checked`);
            
            const correctAnswerKey = qData.correct_answer; 

            // Désactiver tous les boutons radio de la question
            container.querySelectorAll('input[type="radio"]').forEach(radio => radio.disabled = true);

            // Gérer le feedback visuel
            container.querySelectorAll('.option-label').forEach(label => {
                const radio = label.querySelector('input[type="radio"]');
                const optionKey = radio.value;

                if (optionKey === correctAnswerKey) {
                    label.classList.add('correct');
                } else if (selectedOption && optionKey === selectedOption.value) {
                    label.classList.add('incorrect');
                }
            });

            // Calculer le score
            if (selectedOption && selectedOption.value === correctAnswerKey) {
                correctCount++;
            }
        });

        // Afficher le résumé des résultats
        resultsSummary.innerHTML = `Votre Score: ${correctCount} / ${totalQuestions} (${((correctCount / totalQuestions) * 100).toFixed(2)}%)`;
        resultsSummary.style.display = 'block';
    }

    if (quizForm) {
        quizForm.addEventListener('submit', submitQuiz);
    }
});