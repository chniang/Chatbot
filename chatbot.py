# 📚 Importation des bibliothèques
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st
import os

# 📝 Configuration du chemin NLTK personnalisé
NLTK_DATA_PATH = "C:\\Users\\Lenovo\\Desktop\\VSCODE_TRAINING\\myenv\\nltk_data"
if NLTK_DATA_PATH not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_PATH)

# 📥 Téléchargement des ressources nécessaires
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
except Exception:
    pass  # Ignore les erreurs de téléchargement

# 📄 Chargement du fichier texte
FILENAME = "Le livre électronique du projet Gutenberg d'une autre Terre.txt"

lemmatizer = WordNetLemmatizer()
STOP_WORDS = stopwords.words('french')  # Utilisation du français

try:
    with open(FILENAME, 'r', encoding='utf-8') as f:
        data = f.read().replace('\n', ' ')
except FileNotFoundError:
    st.error(f"ERREUR : Le fichier '{FILENAME}' est introuvable. Vérifiez le nom ou le chemin.")
    st.stop()

# ✂︝ Tokenisation en phrases avec PunktSentenceTokenizer
tokenizer = PunktSentenceTokenizer()
sentences = tokenizer.tokenize(data)

# 🔧 Fonction de prétraitement
def preprocess(sentence):
    """
    Nettoie et normalise une phrase : découpage manuel, minuscule, suppression des mots vides/ponctuation, lemmatisation.
    """
    words = sentence.split()
    cleaned_words = []
    for word in words:
        word_lower = word.lower().strip(string.punctuation)
        if word_lower not in STOP_WORDS and word_lower.isalpha():
            cleaned_words.append(lemmatizer.lemmatize(word_lower))
    return cleaned_words

# 🧹 Prétraitement du corpus
corpus = [preprocess(sentence) for sentence in sentences]

# 🔍 Recherche par mots-clés
def get_most_relevant_sentence(query):
    query_keywords = preprocess(query)
    if not query_keywords:
        return "Veuillez poser une question contenant des mots-clés pertinents."

    best_match = ""
    max_overlap = 0

    for i, sentence_tokens in enumerate(corpus):
        overlap = len(set(query_keywords) & set(sentence_tokens))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = sentences[i]

    if max_overlap == 0:
        return "Aucune phrase du livre ne contient les mots-clés de votre question."

    return best_match

# 🤖 Fonction principale du chatbot
def chatbot(question):
    return get_most_relevant_sentence(question)

# 🌝 Interface Streamlit
def main():
    st.set_page_config(page_title="Chatbot Littéraire Français", layout="wide")
    st.title("📚 Chatbot du Livre 'Une autre Terre'")
    st.subheader("Posez une question sur le contenu du livre, et je vous répondrai avec la phrase la plus pertinente.")
    
    question = st.text_input("Votre question :")
    
    if st.button("Obtenir une réponse"):
        if not question:
            st.warning("Veuillez entrer une question.")
            return
        with st.spinner("Recherche en cours..."):
            response = chatbot(question)
            st.write("---")
            st.markdown(f"**Réponse du chatbot :** {response}")

# 🚀 Lancement de l'application
if __name__ == "__main__":
    main()
