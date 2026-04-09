import re

# Fonction de calcul de score
def calculate_score(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else :
        feedback.append("Mot de passe trop court")

    if re.search(r"[A-Z]", password) :
        score += 1
    else :
        feedback.append("Ajouter une majuscule")

    if re.search(r"[a-z]", password) :
        score += 1
    else :
        feedback.append("Ajouter une minuscule")

    if re.search(r"[0-9]", password) :
        score += 1
    else :
        feedback.append("Ajouter un chiffre")

    if re.search(r"[^a-zA-Z0-9]", password) :
        score += 1
    else :
        feedback.append("Ajouter un caractere special")

    return score, feedback

# Recuperer le Mot de passe
password = input("Entrez votre mot de passe : ")

# Calcul du score
score, feedback = calculate_score(password)

# Affichage du score
print("Score : ", score)

# Affichage des ameliorations
for f in feedback :
    print("     - ", f)

# Affichage du niveau de securite du mot de passe
if score <= 2 :
    print("Mot de passe FAIBLE")
elif score <= 4 :
    print("Mot de passe MOYEN")
else :
    print("Mot de passe FORT")