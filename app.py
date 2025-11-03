from flask import Flask, render_template, request, jsonify
from quiz_data import quiz_questions

# Initialisation de l'application
app = Flask(__name__)

# --- Routes de l'application ---

@app.route('/')
def index():
    """Affiche la page d'accueil avec le quiz interactif."""
    return render_template('index.html', questions=quiz_questions)

@app.route('/examen_precedent')
def examen_precedent():
    """Affiche l'image de l'examen de l'année précédente."""
    return render_template('examen_page.html')

@app.route('/ressources')
def ressources():
    """Page d'exemple pour les ressources de préparation."""
    return render_template('ressources.html')

# Lancement du serveur (Non exécuté sur Vercel, mais utile pour le développement local)
if __name__ == '__main__':
    app.run(debug=True)