import os
import sys
from dotenv import load_dotenv

base_dir = os.path.dirname(__file__)
try:
    env_path = os.path.abspath(os.path.join(base_dir, "..", ".env"))
    load_dotenv(dotenv_path=env_path)
except Exception as e:
    print(f"Erreur lors du chargement du fichier .env : {e}")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AnalyzeDoc.views.analyze_api import fetch_data_from_api
from AnalyzeDoc.views.analyze_word import extract_text_from_docx
from AnalyzeDoc.views.analyze_pdf import extract_text_from_pdf
from AnalyzeDoc.views.analyze_text import read_text_from_file
from AnalyzeDoc.views.analyze_excel import extract_text_from_excel
from AnalyzeDoc.general.traity_preprocessed_text import preprocess_text
from AnalyzeDoc.general.preprocessed_text import save_preprocessed_text
from colorama import Fore, Style

doc_paths = [os.path.abspath(os.path.join(base_dir, "dataset", "doc_word2.docx"))] #, os.path.abspath(os.path.join(base_dir, "dataset", "doc_word3.docx")), os.path.abspath(os.path.join(base_dir, "dataset", "doc_word4.docx")), os.path.abspath(os.path.join(base_dir, "dataset", "doc_word5.docx")), os.path.abspath(os.path.join(base_dir, "dataset", "doc_word6.docx"))]
pdf_paths = [os.path.abspath(os.path.join(base_dir, "dataset", "doc_pdf1.pdf")), os.path.abspath(os.path.join(base_dir, "dataset", "doc_pdf2.pdf"))]
text_paths = [os.path.abspath(os.path.join(base_dir, "dataset", "doc_txt1.txt"))]
excel_paths = [os.path.abspath(os.path.join(base_dir, "dataset", "doc_excel1.xlsx"))]

Have_New_Data = os.getenv("Have_New_Data")
Doc_Language = os.getenv("Doc_Language")

data = {
    "docs": doc_paths,
    "pdf": pdf_paths,
    "text": text_paths,
    "excel": excel_paths
}

def get_text_format(data, language):
    """
    Récupère le texte à partir des données fournies.
    Args:
        data (dict): Dictionnaire contenant les données à traiter.
    
    Returns:
            str: Texte extrait des données fournies.
    """

    text = ""
    # API dataset
    text += fetch_data_from_api()

    # Word dataset
    text += extract_text_from_docx(data.get("docs")) if data.get("docs") else ""

    # PDF dataset
    text += extract_text_from_pdf(data.get("pdf")) if data.get("pdf") else ""

    # Text dataset
    text += read_text_from_file(data.get("text")) if data.get("text") else ""

    # Excel dataset
    text += extract_text_from_excel(data.get("excel")) if data.get("excel") else ""
    
    # Traitement du texte
    text_traited = preprocess_text(text)
    # Enregistrement du texte traité dans un fichier
    return save_preprocessed_text(text_traited, language)

def choose_color(text):
    if "Nouvelles données disponibles" in text:
        return Fore.BLUE
    elif "Traitement des données en cours..." in text:
        return Fore.YELLOW
    elif "Traitement des données terminé" in text:
        return Fore.GREEN
    else:
        return Style.RESET_ALL

def launch_main():
    if Have_New_Data == "TRUE":
        print(choose_color("Nouvelles données disponibles") + "Nouvelles données disponibles")
        print(choose_color("Traitement des données en cours...") + "Traitement des données en cours...")
        print(Style.RESET_ALL)
        save_path = get_text_format(data, Doc_Language)
        print(choose_color("Traitement des données terminé") + "Traitement des données terminé")
        print(f"Le texte prétraité est disponible dans le fichier : {save_path}")
        print(Style.RESET_ALL)
    else:
        print(choose_color("Aucune nouvelle donnée") + "Aucune nouvelle donnée")
        print(Style.RESET_ALL)