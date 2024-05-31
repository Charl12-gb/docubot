import re
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):
    text = text.lower()  # Conversion en minuscules
    text = re.sub(r'\s+', ' ', text)  # Suppression des espaces supplémentaires
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)  # Suppression des caractères spéciaux
    return text

def preprocess_text(cleaned_text, language='english'):
    """
    Prétraite le texte en effectuant les étapes suivantes :
    1. Nettoyage du texte
    2. Tokenization
    3. Suppression des stop words
    4. Lemmatisation

    Args:
        text (str): Le texte à prétraiter.
        language (str): La langue du texte ('english' ou 'french').

    Returns:
        str: Le texte prétraité.
    """

    # Télécharger les ressources nécessaires de NLTK
    nltk.download('punkt')
    nltk.download('stopwords')

    # Charger le modèle SpaCy pour la lemmatisation
    if language == 'english':
        nlp = spacy.load('en_core_web_sm')  # Utiliser 'fr_core_news_sm' pour le français
    else:
        nlp = spacy.load('fr_core_news_sm')

    # 1. Tokenization
    words = word_tokenize(cleaned_text)

    # 2. Suppression des stop words
    stop_words = set(stopwords.words(language))
    filtered_words = [word for word in words if word not in stop_words]

    # 3. Lemmatisation
    def lemmatize_words(words):
        doc = nlp(" ".join(words))
        return [token.lemma_ for token in doc]

    lemmatized_words = lemmatize_words(filtered_words)

    # Convertir la liste de mots lemmatisés en une seule chaîne de texte
    preprocessed_text = " ".join(lemmatized_words)

    return preprocessed_text
