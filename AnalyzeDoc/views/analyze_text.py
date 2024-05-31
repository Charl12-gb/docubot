import os
from AnalyzeDoc.general.traity_preprocessed_text import clean_text

def read_text_from_file(file_paths):
    """
    Lecture du texte d'un fichier.

    Args:
        file_paths (list): Chemin du fichier.

    Returns:
        str: Texte extrait du fichier.
    """

    text = ""
    for file_path in file_paths:
        normalized_path = os.path.normpath(file_path)
        if os.path.exists(normalized_path):
            # Obtenir le nom du fichier
            file_name = os.path.basename(file_path)
            # Ajouter le titre du fichier et l'URL
            text += f'[file_name={file_name}][url={file_path}]' + "\n"
            with open(file_path, 'r', encoding='utf-8') as file:
                text += clean_text(file.read()) + "\n"
                text += "\n\n"
    return text