from flask import Flask, render_template, request, jsonify
from quiz_data import quiz_questions

# Initialisation de l'application
app = Flask(__name__)

# --- Routes de l'application ---

@app.route('/')
def index():
    """Affiche la page d'accueil avec le quiz interactif."""
    # Passage des questions au template HTML
    return render_template('index.html', questions=quiz_questions)

@app.route('/examen_precedent')
def examen_precedent():
    """Affiche l'image de l'examen de l'année précédente."""
    return render_template('examen_page.html')

@app.route('/ressources')
def ressources():
    """Page d'exemple pour les ressources de préparation."""
    return render_template('ressources.html')

# Note: Pour un quiz simple, la correction se fait via JavaScript (voir script.js). 
# Pour un système plus avancé, on pourrait ajouter une route POST /submit_quiz

# Lancement du serveur
# app.py (Partie corrigée)
# ... (votre code précédent)

# Lancement du serveur
if __name__ == '__main__':
    # Le mode debug est utile pendant le développement
    # L'erreur est ici : assurez-vous qu'il n'y a PAS de ``` ni de """ après le True)
    app.run(debug=True)