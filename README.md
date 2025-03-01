# IA Générative pour l'Aide à la Recherche de Politiques et Procédures d'Entreprise

## Objectif

Développer une IA générative sous forme de chatbot capable d'aider les employés d'une entreprise à trouver plus facilement des informations dans les politiques, procédures et autres documents importants. De plus, l'application doit gérer les alertes de révision des documents, permettant aux administrateurs de configurer les responsables des documents et de recevoir des notifications avant les dates de révision.

## Fonctionnalités Clés

### 1. Recherche Contextuelle
Permet aux utilisateurs de poser des questions en langage naturel pour trouver des informations dans les documents.

**Exemple :**
```
Utilisateur : Quelle est la politique de congé maladie ?
IA : (Politique N°1 – Nom de la politique) La politique de congé maladie permet aux employés de prendre des congés en cas de maladie justifiée par un certificat médical.
[link document]
```

### 2. Suggestions Proactives
Proposer des documents ou des informations pertinentes basées sur les interactions précédentes.

**Exemple :**
```
Utilisateur : J'ai besoin de plus d'informations sur les congés payés.
IA : Vous pourriez également être intéressé par notre politique de vacances annuelles et les procédures de demande de congé.
[link document]
```

### 3. Suggestion
Proposer des documents ou procédures en fonction de l'historique de recherche ou des besoins exprimés par l'utilisateur.

### 4. Application Web à Ajouter aux Favoris
Permet aux utilisateurs d'ajouter l'application Web à leurs favoris pour un accès rapide.

### 5. Intégration avec d'autres Outils
Intégrer le chatbot avec des outils de communication d'entreprise comme Microsoft Teams ou Slack.

**Exemple :**
```
Utilisateur (dans Slack) : Quelle est la procédure pour demander un remboursement de frais ?
IA : La procédure de remboursement de frais est la suivante : [lien vers le document]. Vous pouvez également la trouver dans notre espace partagé Teams.
```

### 6. Sécurité et Conformité
Gérer l'accès basé sur les rôles et assurer la traçabilité des interactions avec l'IA.

- **Gestion des utilisateurs** :
    - Préchargement des adresses emails
    - Validation après inscription ou connexion via Active Directory
    - Authentification lors du premier accès
    - Rechargement des données (emails)
    - Ajouter un utilisateur
    - Supprimer un utilisateur

### 7. Ajouter un Blog Accessible par Département
Un blog accessible pour chaque département afin de partager les nouvelles informations importantes.

- **Fonctionnalités du blog** :
    - Personnalisable par département
    - Configuration de la date de sauvegarde des données
    - Liste des informations : titre, description, lien
    - Chatbot pour plus de détails sur la nouvelle information
```

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/votre-repository/nom-du-projet.git
    ```

2. Accédez au dossier du projet :
    ```bash
    cd nom-du-projet
    ```

3. Installez les dépendances :
    ```bash
    npm install
    ```

4. Lancer l'application :
    ```bash
    npm start
    ```

## Configuration

1. Configurez les utilisateurs dans le fichier `config/users.json`.
2. Configurez l'intégration avec Microsoft Teams et Slack dans les fichiers de configuration respectifs sous `config/integrations/`.

## Contribution

Si vous souhaitez contribuer à ce projet, merci de suivre ces étapes :

1. Forkez le projet.
2. Créez une branche (`git checkout -b feature-xyz`).
3. Commitez vos changements (`git commit -am 'Add new feature'`).
4. Poussez votre branche (`git push origin feature-xyz`).
5. Créez une Pull Request.
