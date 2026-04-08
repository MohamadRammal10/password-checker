import re

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


password = input("Entrez votre mot de passe : ")
score = calculate_score(password)

print("Score : ", score)