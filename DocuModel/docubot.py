import os
import sys

# Assurez-vous que le chemin vers les modules de votre projet est correctement ajouté
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transformers import GPTJForCausalLM, AutoTokenizer
from dotenv import load_dotenv

base_dir = os.path.dirname(__file__)
try:
    env_path = os.path.abspath(os.path.join(base_dir, "..", ".env"))
    load_dotenv(dotenv_path=env_path)
except Exception as e:
    print(f"Erreur lors du chargement du fichier .env : {e}")


# Définir le chemin de sauvegarde pour le modèle fine-tuné
fine_tuned_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.getenv('Fine_Tuned_Gpt_J_Path', 'fine_tuned/fine_tuned_gpt_j')))

# Créer le répertoire s'il n'existe pas
os.makedirs(fine_tuned_path, exist_ok=True)


# Charger le modèle fine-tuné et le tokenizer
model = GPTJForCausalLM.from_pretrained(fine_tuned_path)
tokenizer = AutoTokenizer.from_pretrained(fine_tuned_path)

# Exemple de question
question = "Quelle est la procédure pour demander des congés ?"
inputs = tokenizer(question, return_tensors='pt')

# Générer la réponse
outputs = model.generate(inputs['input_ids'], max_length=150, num_return_sequences=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
