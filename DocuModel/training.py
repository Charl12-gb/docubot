import os
import sys

# Assurez-vous que le chemin vers les modules de votre projet est correctement ajouté
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transformers import GPTJForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch
from AnalyzeDoc.analyzer_main import launch_main
from AnalyzeDoc.general.preprocessed_text import load_preprocessed_text

# Lancez la fonction principale de l'analyse
launch_main()

# Charger le tokenizer et le modèle GPT-J
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')
tokenizer.pad_token = tokenizer.eos_token
model = GPTJForCausalLM.from_pretrained('EleutherAI/gpt-j-6B')

# Charger les données prétraitées
preprocessed_text, language = load_preprocessed_text()

# Préparer les données pour l'entraînement
texts = preprocessed_text.split('.')

if len(texts) < 2:
    raise ValueError("Not enough texts to split into train and validation sets.")
labels = [0] * len(texts)  # Placeholder pour les labels (pas utilisé pour GPT-J dans ce contexte)

# Tokenizer les textes
encodings = tokenizer(texts, truncation=True, padding=True, max_length=512, return_tensors='pt')

# Définir une classe de dataset personnalisée
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        return item

    def __len__(self):
        return len(self.encodings['input_ids'])

# Créer une instance de CustomDataset avec les encodages fournis
dataset = CustomDataset(encodings)

# Diviser les données en ensembles d'entraînement et de validation
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
if train_size == 0 or val_size == 0:
    raise ValueError("Train or validation dataset is empty after split.")
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

# Définir les arguments d'entraînement pour le modèle
training_args = TrainingArguments(
    output_dir='./results',
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    num_train_epochs=3,
    logging_dir='./logs',
    logging_steps=100,
    save_steps=500,
    eval_strategy="steps",  # Mis à jour ici
    eval_steps=500,
    save_total_limit=2,
)

# Entraîner le modèle
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# Démarrer l'entraînement du modèle
trainer.train()

# Définir le chemin de sauvegarde pour le modèle fine-tuné
fine_tuned_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.getenv('Fine_Tuned_Gpt_J_Path', 'fine_tuned/fine_tuned_gpt_j')))

# Créer le répertoire s'il n'existe pas
os.makedirs(fine_tuned_path, exist_ok=True)

# Sauvegarder le modèle fine-tuné et le tokenizer
model.save_pretrained(fine_tuned_path)
tokenizer.save_pretrained(fine_tuned_path)
