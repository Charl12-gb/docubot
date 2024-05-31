import os
import fitz  # PyMuPDF
from AnalyzeDoc.general.traity_preprocessed_text import clean_text

def extract_text_from_pdf(pdf_paths):
    """
    Extrait le texte à partir de fichiers PDF.

    Args:
        pdf_paths (list): Chemins des fichiers PDF.

    Returns:
        str: Texte extrait des fichiers PDF.
    """
    text = ""

    for pdf_path in pdf_paths:
        normalized_path = os.path.normpath(pdf_path)
        if os.path.exists(normalized_path):
            # Obtenir le nom du fichier
            file_name = os.path.basename(pdf_path)
            # Ajouter le titre du fichier et l'URL
            text += f'[file_name={file_name}][url={pdf_path}]' + "\n"
            try:
                # Ouvrir le fichier PDF
                with fitz.open(normalized_path) as doc:
                    for page in doc:
                        # Obtenir le numéro de la page
                        number_page = page.number
                        text += f'[page={number_page}]' + "\n"
                        # Extraire le texte de chaque page
                        text += clean_text(page.get_text()) + "\n"
                    text += "\n\n"
            except Exception as e:
                text += f"Erreur lors de la lecture du fichier {file_name}: {e}\n"

    return text
