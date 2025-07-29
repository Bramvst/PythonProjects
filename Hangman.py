import random 

geheime_woorden = ["appels","boekenkast","planten","hond","hangman"]

# Hangman game

def run_hangman():
    #Hoeveel pogingen krijgt de speler
    pogingen = 8
    
    #Intro
    print(f"Welkom bij hangman! Je doel is om het woord te raden voordat je dood bent, je krijgt {pogingen} pogingen!")
    
    #Woord random kiezen met random package van python
    geheime_woord = random.choice(geheime_woorden)
    
    #Streepjes tonen waar letters moeten komen
    getoonde_woord = ['_' for i in geheime_woord]
    
    #Loop van het spel
    while pogingen > 0 and '_' in getoonde_woord:
        
        print("\n" + ' '.join(getoonde_woord))
        
        #Input vragen
        gok = input("Geef een letter: ").lower()
        
        #Correcte input
        if gok in geheime_woord:
            for index, letter in enumerate(geheime_woord):
                if letter == gok:
                    getoonde_woord[index] = gok
        #Foute input
        else:
            print(f"Die letter is fout, jammer!")
            pogingen -= 1
    #Winst
    if '_' not in getoonde_woord:
        print(f"Goed gedaan, jij hebt gewonnen!!")
    else:
        print(f"Jammer, volgende keer beter!")
#Spel uitvoeren
run_hangman()