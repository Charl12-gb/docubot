import requests
import os
from AnalyzeDoc.views.analyze_api import *
from AnalyzeDoc.general.traity_preprocessed_text import clean_text

def get_api_urls_from_env():
    api_urls_array = []
    for key, value in os.environ.items():
        if key.startswith("API_URLS"):
            parts = key.split("_")
            index = int(parts[2])
            sub_key = parts[3].lower()
            # Récupérer ou créer un dictionnaire pour cet index
            if len(api_urls_array) <= index:
                api_urls_array.append({})
            # Insérer la valeur dans le dictionnaire correspondant
            api_urls_array[index][sub_key] = value
    return api_urls_array

def launch_api_request(data):
    # Data est un object {url:..., name: ..., token: ...}
    # Vérifier que data contient token
    headers = {}
    if data.get("token"):
        headers = {
            "Content-Type": "application/json",
            "token": data["token"]
        }

    response = requests.post(data.get("url"), headers=headers, json=data.get("body"))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_data_from_api():
    text = ""
    urls = get_api_urls_from_env()
    for api_urls in urls:
        if api_urls.get("url") and api_urls.get("name"):
            data = launch_api_request(api_urls)
            if data:
                # Ajouter le nom et l'url de l'API utilisée
                text += f"[file_name : {api_urls.get('name')}][url : {api_urls.get('url')}]\n"
                # Nettoyer le texte
                text += clean_text(data.get("text"))
                text += text + "\n\n"
        text += "\n"
    return text
