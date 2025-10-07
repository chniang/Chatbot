🤖 Projet Chatbot Retrieval-Based (Corpus Littéraire)
Introduction
Ce projet est un exercice pratique pour la création d'un chatbot de type Retrieval-Based (basé sur la recherche d'informations) utilisant Python et l'interface web Streamlit. L'objectif est de construire un agent conversationnel simple capable de répondre aux questions de l'utilisateur en trouvant la phrase la plus pertinente dans un corpus de connaissances fourni sous forme de fichier texte.

Le sujet choisi pour ce chatbot est basé sur le livre électronique du Projet Gutenberg : "Le livre électronique du projet Gutenberg d'une autre Terre."

⚙️ Architecture et Fonctionnement
Le chatbot utilise des techniques de Traitement Automatique du Langage Naturel (TALN) pour analyser à la fois le corpus de connaissances et la requête de l'utilisateur.

1. Corpus de Connaissances
Fichier Source : Le livre électronique du projet Gutenberg d'une autre Terre.txt

Méthode : Le fichier texte est d'abord tokenisé en phrases, puis chaque phrase est prétraitée pour former le corpus de recherche.

2. Prétraitement (preprocess())
Cette fonction est cruciale pour normaliser le langage et se concentre sur les étapes suivantes :

Tokenisation : Divise la phrase en mots (tokens).

Nettoyage : Convertit tous les mots en minuscules.

Filtrage : Supprime les mots vides (stopwords comme "le", "la", "et") et la ponctuation (string.punctuation).

Normalisation : Applique la Lemmatisation (WordNetLemmatizer) pour réduire les mots à leur forme de base (ex: "courir" au lieu de "courait" ou "courons").

3. Recherche de Pertinence (get_most_relevant_sentence())
La recherche de la meilleure réponse repose sur la mesure de la similarité :

Métrique : Le Coefficient de Jaccard est utilisé pour calculer la similarité entre l'ensemble des mots-clés de la requête de l'utilisateur et l'ensemble des mots-clés de chaque phrase du corpus.

Formule : Jaccard= 
∣Union des Mots∣
∣Mots Communs∣
​
 

Résultat : La fonction retourne la phrase originale du corpus qui a obtenu le score de similarité le plus élevé.

🚀 Instructions d'Installation et d'Exécution
Suivez ces étapes pour installer les dépendances et lancer le chatbot sur votre machine.

Prérequis
Python 3.x

Un environnement virtuel (ex: myenv)

Le fichier corpus (Le livre électronique du projet Gutenberg d'une autre Terre.txt) doit être placé dans le même répertoire que le script Python.

1. Installation des Dépendances
Installez les bibliothèques nécessaires à l'aide de pip :

Bash

pip install nltk streamlit
2. Configuration des Ressources NLTK (Important !)
Si vous rencontrez des erreurs de type LookupError: Resource punkt_tab not found, cela signifie que NLTK n'a pas téléchargé ses fichiers de données dans le bon répertoire. Vous devez exécuter les téléchargements manuellement :

Bash

# 1. Entrez dans l'interpréteur Python de votre environnement
python

# 2. Dans l'interpréteur (>>>), tapez :
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> nltk.download('wordnet')
>>> exit()
3. Lancement de l'Application
Lancez l'interface web du chatbot en utilisant Streamlit :

Bash

streamlit run chatbot.py
Le navigateur par défaut s'ouvrira automatiquement, affichant l'interface du chatbot.

🧪 Personnalisation et Amélioration
Ce projet est une base qui peut être améliorée :

Composant	Idée d'Amélioration
Prétraitement	Ajouter la gestion des acronymes ou l'expansion des contractions.
Similarité	Remplacer le Coefficient de Jaccard par une métrique basée sur les vecteurs comme la Similarité Cosinus (nécessite l'utilisation de TfidfVectorizer ou de modèles d'embeddings).
Réponse	Implémenter une règle de réponse spécifique si le score de similarité dépasse un seuil élevé (ex: "C'est une correspondance exacte ! Voici la phrase: ...").
Corpus	Utiliser un corpus multilingue et détecter la langue de la requête.

(Le code pour ce projet est contenu dans le fichier chatbot.py)
