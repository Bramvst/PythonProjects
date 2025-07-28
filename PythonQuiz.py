# Python project: Eigen quiz

# Hieronder staan de vragen die ik wil stellen

vragen = [
    {"Vraag":"Waar ligt de m. Omohyoideus?",
     "Antwoord":["A. Onder de tong", "B. Onder de knie","C. Onder het hart","D. Onder de enkel"],
     "Correcte_antwoord":"A"},
    
    {"Vraag":"Hoeveel is het wereldrecord deadlift?",
     "Antwoord":["A. 450kg","B. 400kg","C. 535kg","D. 505kg"],
     "Correcte_antwoord":"D"},
    
    {"Vraag":"Wat is de optimale tijd om te rusten tussen sets in training?",
     "Antwoord":["A. 1 a 2 minuten","B. Dat hangt af van jouw doel","C. 3 minuten","D. 4 a 5 minuten"],
     "Correcte_antwoord":"B"},
    
    {"Vraag":"Wat is de betekenis van het woord \"soñar\" in het Spaans?",
     "Antwoord":["A. Toeteren","B. Roepen", "C. Dromen", "D. Lachen"],
     "Correcte_antwoord":"C"},
    
    {"Vraag":"Welke kleur zit er niet in de vlag van Colombia?",
     "Antwoord":["A. Groen","B. Blauw","C. Geel","D. Rood"],
     "Correcte_antwoord":"A"},
    
    {"Vraag":"Wat is een nulhypothese?",
     "Antwoord":["A. Je vermoeden dat het antwoord 0 zal zijn","B. Je vermoeden dat er geen effect zal zijn","C. Je vermoeden dat er wel een effect zal zijn","D. Hetzelfde als je alternatieve hypothese"],
     "Correcte_antwoord":"B"}
    ]
# Ik schrijf een programma dat de quiz uitvoert
def quiz():
    print(f"Er zijn momenteel 5 vragen, gelieve hieronder in te geven hoeveel vragen je wil maken\n")

    # Maak een variabele die de score kan bijhouden
    score = 0
    # Aantal vragen berekenen
    aantal_vragen = input("Gelieve hier een getal van 1 - 5 te geven: ")
    # Maak een teller voor aantal vragen die gemaakt zijn
    gemaakte_vragen = 0

    for vraag in vragen:

        # Print de eerste vraag
        print(vraag["Vraag"])
        # Print de antwoordmogelijkheden
        for optie in vraag["Antwoord"]:
            print(optie)
        # Vraag de speler om een antwoord
        antwoord_speler = input("Geef je antwoord A, B, C of D: ").upper()
        # Bekijk of het antwoord correct is, zo ja +1 anders melding dat het fout is en naar de volgende vraag
        if antwoord_speler == vraag["Correcte_antwoord"]:
            score += 1
            print(f"Dat is het juiste antwoord!\n")
        else:
            print(f"Dat is niet correct!\n")
        gemaakte_vragen += 1
        if gemaakte_vragen == int(aantal_vragen):
            break
    # Geef aan wat de eindscore is
    print(f"Jouw score op deze test der wijsheid is {score} op {aantal_vragen} .")

# Intro
print(f" Hallo, leuk dat je deze quiz wil maken!\n") 
while True:
    quiz()
    Einde = input("Wil je stoppen?(J/N): ").upper()
    if Einde == "J":
        print(f"Bedankt om deel te nemen, tot de volgende keer!")
        break