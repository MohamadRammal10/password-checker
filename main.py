import re

# Fonction de calcul de score
def calculate_score(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) :
        score += 1
    if re.search(r"[a-z]", password) :
        score += 1
    if re.search(r"[0-9]", password) :
        score += 1
    if re.search(r"[^a-zA-Z0-9]", password) :
        score += 1

    return score

# Recuperer le Mot de passe
password = input("Entrez votre mot de passe : ")

# Calcul du score
score = calculate_score(password)

# Affichage du score
print("Score : ", score)

# Affichage du niveau de securite du mot de passe
if score <= 2 :
    print("Mot de passe FAIBLE")
elif score <= 4 :
    print("Mot de passe MOYEN")
else :
    print("Mot de passe FORT")