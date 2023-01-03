import random

# ctrl+w ftw

print("Siemano witam w mojej kuchni!\nDawaj pierdolniemy sb w kamien papier andżej")

twoje_punkty = 0
punkty_kompa = 0

# The loop should not start if user or computer score is already 3 or more
# - should start only when both user and computer points are less than 3
while twoje_punkty < 3 and punkty_kompa < 3:
    # print(f'na poczatku loopa:{twoje_punkty}:{punkty_kompa}')
    # Take user input as a sign

    wybor_chlopa = input("\nPodaj co wybierasz (kamień - wpisz \"k\", papier - \"p\", nożyce - \"n\"):\n")

    if wybor_chlopa == 'k':
        print("wybrales kamien gamoniu")
    elif wybor_chlopa == 'p':
        print("papier to do dupy sie nadaje")
    elif wybor_chlopa == 'n':
        print("nożyce nożyce jebac kurwa widzew")
    else:
        print("chyba sie z chujem na glowe zamieniles")
        continue

    # Make computer chose a hand sign...

    wybor_kompa = random.choice(['k', 'p', 'n'])
    print(f'Komp wybrał: {wybor_kompa}')

    kombinacja = wybor_chlopa + wybor_kompa
    print(f'Kombinacja w tej rundzie: {kombinacja}')

    # If a draw continue a loop and don't increase a score
    if wybor_chlopa == wybor_kompa:
        print("Remis kurwa. Jeszcze raz.")
        continue

    elif kombinacja == 'np' or kombinacja == 'pk' or kombinacja == 'kn':
        print("No tym razem wygrales kurwiu")
        twoje_punkty += 1
    else:
        print("Komp wygrał te runde.")
        punkty_kompa += 1

    print(f'Obecny wynik Ty:{twoje_punkty}, Komp:{punkty_kompa}')

print("Koniec kurwa!")
