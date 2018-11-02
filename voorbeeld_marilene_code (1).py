import Score_program

antwoord = ''
munten = 25

while True:
    antwoord_gebruiker = input('Is een bal rond? (ja/nee/hint)')

    if antwoord_gebruiker == 'ja':
        antwoord = 'correct'
        break
    elif antwoord_gebruiker == 'nee':
        antwoord = 'incorrect'
        break
    elif antwoord_gebruiker == 'hint':
        antwoord = 'hint'
        munten = Score_program.update_score(antwoord, munten)

uitslag = Score_program.update_score(antwoord, munten)
print('je score is: ' + str(uitslag))

Score_program.store_points('Rijk')


