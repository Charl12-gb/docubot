import pandas as pd
import os
from AnalyzeDoc.general.traity_preprocessed_text import clean_text

def preprocess_excel(excel_path):
    """
    Prétraite un fichier Excel en effectuant plusieurs traitements.

    Args:
        excel_path (str): Chemin du fichier Excel.

    Returns:
        str: Texte extrait et prétraité du fichier Excel.
    """
    try:
        # Obtenir le nom du fichier Excel
        excel_name = os.path.basename(excel_path)

        # Lecture du fichier Excel
        df = pd.read_excel(excel_path)
        
        # Suppression des doublons
        df = df.drop_duplicates()
        
        # Nettoyage des données
        # df = df.dropna()  # Suppression des lignes avec des valeurs manquantes
        
        # Concaténation de toutes les colonnes en une seule chaîne de caractères
        text = " ".join(df.apply(lambda x: " ".join(map(str, x)).lower(), axis=1)) 
        text = f'[file_name={excel_name}][url={excel_path}]' + "\n" + clean_text(text)

        return text
    except Exception as e:
        print(f"Erreur lors du prétraitement du fichier Excel : {e}")
        return ""

def extract_text_from_excel(excel_paths):
    """
    Extrait le texte à partir de fichiers Excel.

    Args:
        excel_paths (list): Chemins des fichiers Excel.

    Returns:
        str: Texte extrait des fichiers Excel.
    """
    try:
        # Prétraitement des fichiers Excel
        text = ""
        for excel_path in excel_paths:
            preprocessed_text = preprocess_excel(excel_path)
            if preprocessed_text:
                text += preprocessed_text + "\n\n"
        
        return text
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte depuis les fichiers Excel : {e}")
        return ""
