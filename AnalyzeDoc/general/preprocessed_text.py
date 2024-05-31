import pickle
import os
import sys

base_dir = os.path.dirname(__file__)
load_preprocessed_text_path = os.path.abspath(os.path.join(base_dir, "..", "dataset", "preprocessed_text.pkl"))

def save_preprocessed_text(text, language):
    """
    Sauvegarde le texte prétraité dans un fichier.

    Args:
        text (str): Le texte prétraité.
        language (str): La langue du texte ('english' ou 'french').

    Returns:
        str: Le chemin du fichier.
    """
    try:
        with open(load_preprocessed_text_path, 'wb') as file:
            pickle.dump((text, language), file)
        return load_preprocessed_text_path
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du texte prétraité : {e}")
        return ""

def load_preprocessed_text():
    """
    Charge le texte prétraité à partir d'un fichier avec un affichage de pourcentage de progression.

    Returns:
        tuple: Un tuple contenant le texte prétraité et la langue.
    """
    try:
        file_size = os.path.getsize(load_preprocessed_text_path)
        with open(load_preprocessed_text_path, 'rb') as file:
            chunk_size = 1024  # Taille des chunks en octets
            loaded_size = 0
            buffer = b""

            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                buffer += chunk
                loaded_size += len(chunk)
                percentage = (loaded_size / file_size) * 100
                sys.stdout.write(f"\rChargement du texte prétraité : {percentage:.2f}%")
                sys.stdout.flush()

            text, language = pickle.loads(buffer)
            print("\nChargement terminé.")
            return text, language

    except Exception as e:
        print(f"Erreur lors du chargement du texte prétraité : {e}")
        return None, None
        