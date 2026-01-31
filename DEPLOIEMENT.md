# Guide de déploiement pour une nouvelle agence

## 1. Récupérer le projet
```bash
git clone [url-du-repo]
cd gcl-questionnaire
```

## 2. Configuration du cabinet

### Copier le fichier de configuration
```bash
cp .env.example .env
```

### Éditer `.env` avec les informations de VOTRE cabinet
```bash
nano .env  # ou vim, ou votre éditeur préféré
```

**Variables à modifier OBLIGATOIREMENT :**
- `CABINET_NAME` : Nom complet de votre cabinet
- `CABINET_ADDRESS` : Adresse postale
- `CABINET_EMAIL` : Email de contact
- `CABINET_PHONE` : Téléphone
- `SECRET_KEY` : Générer une nouvelle clé (voir ci-dessous)
- `INSEE_API_KEY` : Votre clé API INSEE

### Générer une SECRET_KEY unique
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 3. Installation et démarrage
```bash
# Créer l'environnement virtuel
uv venv
source .venv/bin/activate

# Installer les dépendances
uv pip install -r requirements.txt

# Initialiser la base de données
python manage.py migrate
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

## 5. Vérification

Vérifier que partout s'affiche le nom de VOTRE cabinet, pas "Cabinet Tartampion".

## Support

En cas de problème : [votre contact]