# 🔐 Password Strength Checker

## 📌 Description

Ce projet est un outil de cybersécurité permettant d’évaluer la robustesse d’un mot de passe selon plusieurs critères de sécurité.

Il fournit un score, des recommandations d’amélioration et une estimation du temps nécessaire pour casser le mot de passe par attaque brute-force.

---

## 🚀 Fonctionnalités

* ✅ Analyse de la longueur du mot de passe
* ✅ Détection de :

  * majuscules
  * minuscules
  * chiffres
  * caractères spéciaux
* ✅ Score de sécurité (faible / moyen / fort)
* ✅ Feedback détaillé pour améliorer le mot de passe
* ✅ Détection de mots de passe courants
* ✅ Estimation du temps de cassage (brute-force)
* ✅ Affichage du temps en années, jours, heures, minutes et secondes

---

## 🛠️ Technologies utilisées

* Python 3
* Regex (`re`)
* Colorama (affichage en couleur)

---

## 📂 Structure du projet

```
password-checker/
├── main.py
├── common_passwords.txt
├── README.md
```

---

## ▶️ Utilisation

### 1. Cloner le projet

```bash
git clone https://github.com/TON_USERNAME/password-checker.git
cd password-checker
```

### 2. Installer les dépendances

```bash
pip install colorama
```

### 3. Lancer le programme

```bash
python main.py
```

---

## 💡 Exemple

```
Entrez votre mot de passe : Test123

Score : 3
Mot de passe MOYEN

Améliorations :
- Ajouter un caractère spécial

Temps estimé pour casser le mot de passe : 2 heures 15 minutes 10 secondes
```

---

## 🎯 Objectif du projet

Ce projet a été réalisé dans le cadre d’un apprentissage en cybersécurité afin de comprendre :

* les bonnes pratiques de création de mots de passe
* les bases des attaques par brute-force
* l’importance de l’entropie

---

## ⚠️ Avertissement

Ce projet est éducatif.
Les estimations de temps sont approximatives et ne reflètent pas les capacités réelles des attaquants modernes (GPU, dictionnaires, etc.).

---

## 📈 Améliorations futures

* Interface graphique (Tkinter / Web)
* API REST
* Intégration dans un outil de sécurité
* Analyse avancée (patterns, répétitions)

---

## 👨‍💻 Auteur

Mohamad RAMMAL
