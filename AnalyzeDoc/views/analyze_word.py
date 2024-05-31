import os
from docx import Document
from AnalyzeDoc.general.traity_preprocessed_text import clean_text

def extract_text_from_docx(doc_paths):
    """
    Extrait le texte des fichiers docx.

    Args:
        doc_paths (list): Chemins des fichiers docx.

    Returns:
        str: Texte extrait des fichiers docx.
    """

    text = ""

    for docx_path in doc_paths:
        normalized_path = os.path.normpath(docx_path)
        if os.path.exists(normalized_path):
            # Obtenir le nom du fichier
            file_name = os.path.basename(docx_path)
            # Ajouter le titre du fichier et l'URL
            text += f'[file_name={file_name}][url={docx_path}]' + "\n"
            try:
                doc = Document(normalized_path)
                for para in doc.paragraphs:
                    # Extraire le texte de chaque paragraphe
                    text += clean_text(para.text) + "\n"
                text += "\n\n"
            except Exception as e:
                text += f"Erreur lors de la lecture du fichier {file_name}: {e}\n"
    return text
