# 📊 Questionnaire Facturation Électronique 2026

[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Application web Django permettant aux cabinets d'expertise comptable de réaliser un diagnostic auprès de leurs clients dans le cadre de la réforme de la facturation électronique obligatoire au 1er septembre 2026.

## 📋 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Déploiement](#-déploiement)
- [Structure du projet](#-structure-du-projet)
- [Technologies utilisées](#-technologies-utilisées)
- [Licence](#-licence)
- [Support](#-support)

## 🎯 À propos

Ce projet permet aux cabinets comptables de :
- Collecter les informations sur l'équipement actuel de leurs clients
- Évaluer leur niveau de préparation à la facturation électronique
- Centraliser les données dans un dashboard collaborateur
- Exporter les résultats pour analyse

### Contexte réglementaire

À partir du **1er septembre 2026**, toutes les entreprises assujetties à la TVA devront émettre et recevoir leurs factures au format électronique, avec transmission obligatoire via une plateforme agréée (ex: Chorus Pro).

## ✨ Fonctionnalités

### 👥 Parcours Client
- ✅ Questionnaire accessible sans authentification
- ✅ Validation automatique du SIREN via API INSEE
- ✅ Détection des questionnaires déjà remplis
- ✅ Sauvegarde automatique (localStorage)
- ✅ Barre de progression dynamique
- ✅ Interface responsive et accessible

### 👔 Parcours Collaborateur
- ✅ Authentification sécurisée avec protection brute-force (Django Axes)
- ✅ Dashboard avec statistiques
- ✅ Filtres et recherche avancée
- ✅ Visualisation détaillée des questionnaires
- ✅ Vue synthétique comparant réponses client/collaborateur
- ✅ Export CSV complet
- ✅ Archivage des entreprises

### 🔐 Sécurité
- ✅ Protection CSRF
- ✅ Sessions sécurisées (4h)
- ✅ Protection contre les attaques brute-force
- ✅ Conformité RGPD
- ✅ Cookies essentiels uniquement

### 🎨 Multi-agence
- ✅ Configuration par variables d'environnement
- ✅ Personnalisation : nom, adresse, contacts
- ✅ Déploiements indépendants par cabinet

## 🛠️ Prérequis

- **Python** 3.12+
- **uv** (gestionnaire de paquets Python)
- **MySQL** 5.7+ ou **PostgreSQL** 13+ (en production)
- **Clé API INSEE** (gratuite) : [api.insee.fr](https://api.insee.fr/)

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/UTurtleDev/gcl.git
cd gcl
```

### 2. Créer l'environnement virtuel
```bash
uv venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

### 3. Installer les dépendances
```bash
uv pip install -r requirements.txt
```

### 4. Configuration
```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer avec vos valeurs
nano .env
```

**Variables obligatoires à modifier :**
```bash
# Cabinet
CABINET_NAME="Votre Cabinet"
CABINET_ADDRESS="Votre adresse"
CABINET_EMAIL="contact@votrecabinet.fr"
CABINET_PHONE="01 XX XX XX XX"

# Sécurité (générer une nouvelle clé)
SECRET_KEY=votre-clé-secrète-unique

# API INSEE
INSEE_API_KEY=votre-clé-api-insee
```

### 5. Générer une SECRET_KEY
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 6. Initialiser la base de données
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Lancer le serveur de développement
```bash
python manage.py runserver
```

Accéder à : **http://localhost:8000**

## ⚙️ Configuration

### Variables d'environnement

| Variable | Description | Exemple |
|----------|-------------|---------|
| `CABINET_NAME` | Nom du cabinet | `"Cabinet Tartampion"` |
| `CABINET_ADDRESS` | Adresse postale | `"1 rue des Champs Elysées - 75008 PARIS"` |
| `CABINET_EMAIL` | Email de contact | `"contact@tartampion.fr"` |
| `CABINET_PHONE` | Téléphone | `"01 23 45 67 89"` |
| `SECRET_KEY` | Clé secrète Django | Générer avec `secrets` |
| `DEBUG` | Mode debug | `True` (dev) / `False` (prod) |
| `ALLOWED_HOSTS` | Domaines autorisés | `localhost,votredomaine.fr` |
| `INSEE_API_KEY` | Clé API INSEE | Obtenir sur api.insee.fr |

#### Couleurs
Modifier les variables CSS dans `static/base/css/base.css` et `static/questionnaires/css/styles.css` :
```css
:root {
    --bleue-fonce: #012F8B;
    --bleue-moyen: #0048B7;
    --bleue-clair: #006EE1;
}
```

## 🌐 Déploiement

### Production (o2switch / serveur Linux)

#### 1. Préparer l'environnement
```bash
# Sur le serveur
cd ~/votre-projet
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

#### 2. Configurer `.env` pour la production
```bash
DEBUG=False
ALLOWED_HOSTS=votredomaine.fr,www.votredomaine.fr

# Base de données MySQL
USE_MYSQL=True
DB_ENGINE=django.db.backends.mysql
DB_NAME=votre_db
DB_USER=votre_user
DB_PASSWORD=votre_password
DB_HOST=localhost
DB_PORT=3306
```

#### 3. Déployer
```bash
# Migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
```

## 📁 Structure du projet
```
gcl/
├── config/                  # Configuration Django
│   ├── settings.py         # Paramètres principaux
│   ├── urls.py             # Routes principales
│   ├── context_processors.py  # Variables globales templates
│   └── wsgi.py
│
├── questionnaires/         # Application principale
│   ├── models.py           # Modèles (Entreprise, Questionnaires)
│   ├── views.py            # Vues et logique métier
│   ├── forms.py            # Formulaires Django
│   ├── urls.py             # Routes de l'app
│   ├── admin.py            # Interface d'administration
│   └── utils.py            # Utilitaires (API INSEE)
│
├── users/                  # Gestion des utilisateurs
│   └── models.py           # User personnalisé
│
├── templates/              # Templates HTML
│   ├── base.html           # Template de base
│   └── questionnaires/
│       ├── home.html
│       ├── client/
│       └── collaborateur/
│
├── static/                 # Fichiers statiques
│   ├── base/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── questionnaires/
│       ├── css/
│       └── js/
│
├── .env.example            # Template de configuration
├── requirements.txt        # Dépendances Python
├── manage.py              # CLI Django
└── README.md              # Ce fichier
```

## 🔧 Technologies utilisées

### Backend
- **Django 6.0** - Framework web Python
- **Django Environ** - Gestion des variables d'environnement
- **Django Axes** - Protection brute-force
- **PyMySQL** - Connecteur MySQL
- **Requests** - Appels API (INSEE)

### Frontend
- **HTML5 / CSS3** - Vanilla (sans framework)
- **JavaScript** - ES6+ (autosave, progression)
- **HTMX** - Interactivité dynamique (validation SIREN)

### Base de données
- **SQLite** - Développement
- **MySQL / PostgreSQL** - Production

### APIs externes
- **API INSEE Sirene 3.11** - Validation et récupération des entreprises

## 🧪 Développement

### Ajouter un nouveau cabinet

1. Dupliquer le projet
2. Modifier `.env` avec les nouvelles valeurs
3. Changer le logo dans `static/base/images/`
4. Déployer sur un nouveau domaine

### Commandes utiles
```bash
# Créer une migration
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Collecter les statiques
python manage.py collectstatic

# Shell Django
python manage.py shell

# Exporter les données
python manage.py dumpdata > backup.json
```

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
```
MIT License

Copyright (c) 2026 UTurtleDev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[...]
```

## 📞 Support

### Pour les utilisateurs (cabinets)

- **Email** : support@votresupport.fr
- **Documentation** : Voir `DEPLOIEMENT.md`

### Pour les développeurs

- **Issues** : [GitHub Issues](https://github.com/UTurtleDev/gcl/issues)
- **Pull Requests** : Bienvenues !

## 🙏 Remerciements

- **Cabinet GCL** - Client initial et cahier des charges
- **API INSEE** - Fourniture gratuite de l'API Sirene
- **Django Community** - Framework exceptionnel

---

**Développé par [UTurtleDev](https://github.com/UTurtleDev)**

*Projet réalisé dans le cadre de la réforme de la facturation électronique 2026*