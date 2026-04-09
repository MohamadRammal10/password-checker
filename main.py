import re

# Fonction de calcul de score, de faire la liste d'amelioration et de trouver le temps de cassage du mot de passe
def calculate_score(password):
    score = 0
    feedback = []
    charset = 0

    password_length = len(password)

    if password_length >= 8:
        score += 1
    else :
        feedback.append("Mot de passe trop court")

    if re.search(r"[A-Z]", password) :
        score += 1
        charset += 26
    else :
        feedback.append("Ajouter une majuscule")

    if re.search(r"[a-z]", password) :
        score += 1
        charset += 26
    else :
        feedback.append("Ajouter une minuscule")

    if re.search(r"[0-9]", password) :
        score += 1
        charset += 10
    else :
        feedback.append("Ajouter un chiffre")

    if re.search(r"[^a-zA-Z0-9]", password) :
        score += 1
        charset += 32    # estimation realiste des caracteres speciaux
    else :
        feedback.append("Ajouter un caractere special")

    # Calcul du temps de cassage en secondes
    combinations = charset ** password_length
    guesses_per_sec = 1e9    # 1 milliard/sec

    seconds = combinations / guesses_per_sec

    return score, feedback, seconds

# Fonction pour detecter les mots de passe courant
def is_common_password(password) :
    with open("common_passwords.txt", "r") as f :
        common = f.read().splitlines()
    return password in common

# Fonction pour changer le format du temps
def format_time(seconds) :
    seconds = int(seconds)

    years = seconds // (365 * 24 * 3600)
    seconds %= (365 * 24 * 3600)

    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    result = []

    if years > 0 :
        result.append(f"{years} annees")
    if days > 0 :
        result.append(f"{days} jours")
    if hours > 0 :
        result.append(f"{hours} heures")
    if minutes > 0 :
        result.append(f"{minutes} minutes")
    if seconds > 0 or not result :
        result.append(f"{seconds} secondes")

    return " ".join(result)

# Recuperer le Mot de passe
password = input("Entrez votre mot de passe : ")

# Calcul du score, feedback et temps de cassage
score, feedback, crack_time_sec = calculate_score(password)
formatted_crack_time = format_time(crack_time_sec)

# Affichage du score
print("Score : ", score)

# Affichage du niveau de securite du mot de passe
if score <= 2 :
    print("Mot de passe FAIBLE")
elif score <= 4 :
    print("Mot de passe MOYEN")
else :
    print("Mot de passe FORT")

# Affichage des ameliorations
for f in feedback :
    print("     - ", f)

# Affichage si mot de passe courant
if is_common_password(password) :
    print("Mot de passe tres courant !!")

# Affichage de l'estimation de temps de cassage du mot de passe
print("Temps estime pour casser le mot de passe : ", formatted_crack_time)