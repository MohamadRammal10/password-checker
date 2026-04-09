# 🔐 Password Strength Checker

## 📌 Description

Password Strength Checker est un outil de cybersécurité développé en Python permettant d’évaluer la robustesse d’un mot de passe.

Il analyse plusieurs critères de sécurité et fournit :

* un score de sécurité
* un retour détaillé pour améliorer le mot de passe
* une estimation du temps nécessaire pour le casser via une attaque brute-force

---

## 🚀 Fonctionnalités

* 🔍 Analyse de la longueur du mot de passe
* 🔠 Détection des majuscules et minuscules
* 🔢 Détection des chiffres
* 🔣 Détection des caractères spéciaux
* 📊 Calcul d’un score de sécurité
* 🧠 Feedback détaillé pour améliorer le mot de passe
* ⚠️ Détection des mots de passe courants (liste locale)
* ⏱️ Estimation du temps de cassage (brute-force)
* 🕒 Affichage du temps en :

  * années
  * jours
  * heures
  * minutes
  * secondes
* 🎨 Affichage coloré dans le terminal

---

## 🛠️ Technologies utilisées

* Python 3
* Regex (`re`)
* colorama

---

## 📂 Structure du projet

```bash
password-checker/
├── main.py
├── common_passwords.txt
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/TON_USERNAME/password-checker.git
cd password-checker
```

---

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
```

---

### 3. Activer l’environnement

```bash
source venv/bin/activate
```

---

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

```bash
python main.py
```

---

## 💡 Exemple

```
Entrez votre mot de passe : Test123

Score : 3
MOYEN

Améliorations :
- Ajouter un caractère spécial

Temps estimé pour casser le mot de passe :
2 heures 15 minutes 10 secondes
```

---

## 📚 Objectif pédagogique

Ce projet permet de comprendre :

* les bonnes pratiques de sécurité des mots de passe
* le principe des attaques par brute-force
* l’importance de la complexité et de l’entropie

---

## ⚠️ Avertissement

Ce projet est à but éducatif uniquement.
Les estimations de temps sont approximatives et ne reflètent pas les capacités réelles des attaquants modernes (GPU, dictionnaires, etc.).

---

## 📈 Améliorations futures

* Interface graphique (Tkinter ou Web)
* API REST
* Analyse avancée (patterns, répétitions)
* Intégration dans un outil de cybersécurité

---

## 👨‍💻 Auteur

Mohamad RAMMAL
