import os
import datetime

#kan eruit als de functies in de GUI geschreven wordt
min_points = 0
points = 25
question = 'correct'
name = 'naam'

def update_score(question, points):
    """ This function updates the score after a question is answered

    the result depends on if the question is correct
    then the score is maximum
    when the result is incorrect the player will get no points
    when a hint is requested three points are deducted from the score
    input is the result of the question and the current score/number of points
    output is the result as described above.
    """
    if question == 'correct':
        return(points)
    elif question == 'incorrect':
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

    the inputs are the points from the temp_totalscore file and use the dayscores.txt to store the total score
    the totaldayscore.txt is to store the score for a the total dayscore
    the totaldayscore are the highest scores from players.
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

def update_highscore(name, points):
    """ This function updates the highscores

    it updates the highscore when the last score is higher than the current highscore or there aren't highscores.
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
                        sortedscores_list = sorted_scores[:10]
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

def change_totaldayscores():
    """This function changes the day if necessary

    first the two files are opened
    when the current day is higher then the last day: the day will be changed and the file dayscores will be emptied
    else nothing"""
    with open('totaldayscores.txt', 'r+') as dayscores, open('date.txt', 'r+') as dates:
        dates_readers = dates.readlines()
        for line in dates_readers:
            last_day = dates_readers[0]
            year = datetime.date.today().strftime('%Y')
            month = datetime.date.today().strftime('%B')
            day = datetime.date.today().strftime('%d')
            date_now = year + '-' + month + '-' + day
            with open('date.txt', 'w') as dates:
                if date_now > last_day:
                    dates.write(date_now)
                    dayscores.seek(0)
                    dayscores.truncate()
                else:
                    dates.write(last_day)



points = update_score(question, points)
save_points(points)
store_points(name)
update_highscore(name, points)
change_totaldayscores()