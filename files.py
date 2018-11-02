def score_dayscore():
    with open('totaldayscores.txt', 'r') as dayscore_file:
        dayscore_reader = dayscore_file.readlines()

    return (dayscore_reader)

print(score_dayscore())