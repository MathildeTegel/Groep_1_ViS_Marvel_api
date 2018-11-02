import os

#kan eruit als de functies in de GUI geschreven wordt
min_points = 0
points = 25


def update_score(question, points):
    """ This function updates the score after a question is answered

    the result depends on if the question is correct
    then the score is maximum
    when the result is incorrect there is one point deducted from the score
    when a hint is requested three points are deducted from the score
    input is the result of the question and the current score/number of points
    output is the result as described above.
    """
    if question == 'correct':
        save_points(points)
        return(points)
    elif question == 'incorrect':
        save_points(points)
        return(min_points)
    elif question == 'hint':
        return(points-3)

def save_points(points):
    """ This function safes the points from a question into a file

    there is one input: points
    the name and score will be safed
    until the score is stored.
    """
    with open('temp_questionscores.txt', 'a') as score_writer:
        score_writer.write(str(points) + ',')

def store_points(name):
    """ This function will store the scores from a person

    the input are the points from the temp_totalscore file and use the dayscores.txt to store the total score
    the totaldayscore.txt is to store the score for a the total dayscore.
    """
    with open('dayscores.txt', 'r+') as store, open('totaldayscores.txt', 'a') as total_dayscore, open('temp_questionscores.txt', 'r') as temp_questionscore:
        question_reader = temp_questionscore.readlines()
        totalscore = question_reader[0]
        totalscore = totalscore.split(',')
        totaal = 0
        for score in totalscore:
            try:
                totaal += int(score)
            except ValueError:
                break
        store.write(name + ':' + str(totaal) + '\n')
        total_dayscore.write(name + ':' + str(totaal) + '\n')
    os.remove('temp_questionscores.txt')

def update_highscore(name, points):
    """ This function updates the highscores

    it updates the highscore when the last score is higher than the current highscore.
    """
    sorted_scores = list()
    with open('dayscores.txt', 'r') as dayscore_file, open('alltimehigh.txt', 'r+') as highscore_file:
        dayscore_reader = dayscore_file.readlines()
        highscore_reader = highscore_file.readlines()
        for line in highscore_reader:
            line = line.replace('\n', '')
            sorted_scores.append(line)
            sorted_scores.sort(reverse=True)
        if int(len(sorted_scores)) > 0:
            minimum_highscore = min(sorted_scores)
            list_min = minimum_highscore
            min_highscore = list_min.split(':')[1]
            for line in dayscore_reader:
                line.split(':')
                score_dayscore = list_min.split(':')[1]
                if int(score_dayscore) > int(min_highscore):
                    with open('alltimehigh.txt', 'w') as highscore_file:
                        scoreline = line.strip()
                        sorted_scores.append(str(scoreline))
                        sorted_scores.sort(reverse=True)
                        sorted_scores_list = sorted_scores[:10]
                        for items in sorted_scores:
                            highscore_file.write("%s\n" % items)
        else:
            for line in dayscore_reader:
                line.split(':')
                score_dayscore = line.split(':')[1]
                with open('alltimehigh.txt', 'w') as highscore_file:
                    scoreline = line.strip()
                    sorted_scores.append(str(scoreline))
                    sorted_scores.sort(reverse=True)
                    sortedscores_list = sorted_scores[:10]
                    for items in sorted_scores:
                        highscore_file.write("%s\n" % items)

#points = update_score(question, points)
#save_points(points)
#store_points(name)
#update_highscore(name, points)



