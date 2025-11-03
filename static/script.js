// script.js

document.addEventListener('DOMContentLoaded', () => {
    // Le tableau quizQuestions est injecté dans index.html via Jinja2

    const quizForm = document.getElementById('quiz-form');
    const submitButton = document.getElementById('submit-button');
    const resultsSummary = document.getElementById('results-summary');

    // --- Logique du Timer ---
    const timerElement = document.getElementById('timer');
    let timeLimitMinutes = 60; // Par exemple, 60 minutes
    let timeRemainingSeconds = timeLimitMinutes * 60;
    let timerInterval;

    function formatTime(totalSeconds) {
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    function startTimer() {
        timerInterval = setInterval(() => {
            if (timeRemainingSeconds <= 0) {
                clearInterval(timerInterval);
                timerElement.textContent = "Temps écoulé !";
                submitQuiz(new Event('submit')); // Soumet le quiz automatiquement
            } else {
                timeRemainingSeconds--;
                timerElement.textContent = formatTime(timeRemainingSeconds);
            }
        }, 1000);
    }

    // Démarre le timer au chargement
    startTimer();

    // --- Logique de Soumission du Quiz ---

    function submitQuiz(event) {
        event.preventDefault(); // Empêche l'envoi du formulaire traditionnel

        let correctCount = 0;
        const totalQuestions = quizQuestions.length;

        // 1. Désactiver le timer et le bouton de soumission
        clearInterval(timerInterval);
        submitButton.disabled = true;

        quizQuestions.forEach(qData => {
            const container = document.querySelector(`.question-container[data-id="${qData.id}"]`);
            if (!container) return; // Sécurité

            const questionName = `q_${qData.id}`;
            const selectedOption = document.querySelector(`input[name="${questionName}"]:checked`);
            
            // Récupérer l'option correcte depuis les données passées
            const correctAnswerKey = qData.correct_answer; 

            // Désactiver tous les boutons radio de la question
            container.querySelectorAll('input[type="radio"]').forEach(radio => radio.disabled = true);

            // Gérer le feedback visuel
            container.querySelectorAll('.option-label').forEach(label => {
                const radio = label.querySelector('input[type="radio"]');
                const optionKey = radio.value;

                if (optionKey === correctAnswerKey) {
                    // C'est la bonne réponse
                    label.classList.add('correct');
                } else if (selectedOption && optionKey === selectedOption.value) {
                    // C'est la réponse de l'utilisateur, mais elle est fausse
                    label.classList.add('incorrect');
                }
            });

            // 2. Calculer le score
            if (selectedOption && selectedOption.value === correctAnswerKey) {
                correctCount++;
            }
        });

        // 3. Afficher le résumé des résultats
        resultsSummary.innerHTML = `Votre Score: ${correctCount} / ${totalQuestions} (${((correctCount / totalQuestions) * 100).toFixed(2)}%)`;
        resultsSummary.style.display = 'block';
    }

    quizForm.addEventListener('submit', submitQuiz);
});