import json
import random
import utility_commands


def create_databases():

    usable_file = open('usable_characters_database.txt', 'w')
    #File leading to database with characters usable for questions
    not_usable_file = open('not_usable_characters_database.txt', 'w')
    #File leading to names of characters not usable for questions, but usable for multiple choice
    numberlist_file = open('usable_numberlist.txt', 'w')
    #File for later with the max index for the usable and unusable characters
    numberlist = []
    #Temp list with usable calls

    character_to_call = 0
    character_limit = 1491
    # Actually sets the offset for the call, starting at 0
    # last character_to_call is 1491 (2018-10-05)
    # OPTIONAL: find a way to find the character limit before database calls


    key_to_choose = input('Voer de key in (1, 2 of 3): ')
    print(f'Creating database with key {key_to_choose}... this might take a while!')
    # Sets the key data that will be used for the API call

    while character_to_call != character_limit:
        hero_comics = []
        hero_series = []
        #creates lists

        connection_url = utility_commands.create_url(character_to_call, key_to_choose)
        print(connection_url)
        #creates url to call
        response = requests.get(connection_url)
        #reply from server
        jsontext = json.loads(response.text)
        #converts to json code
        hero_id = jsontext['data']['results'][0]['id']
        hero_name = jsontext['data']['results'][0]['name']
        hero_description = jsontext['data']['results'][0]['description']
        hero_description = hero_description.replace('\r', '').replace('\n', '')
        #hero_description = utility_commands.fix_database_data(hero_description)
        #finds the ID, name and description of the hero

        if len(hero_description) > 10:
            for item in jsontext['data']['results'][0]['comics']['items']:
                hero_comics.append(item['name'])

            for item in jsontext['data']['results'][0]['series']['items']:
                hero_series.append(item['name'])
            #adds comic and serie information if character has an actual description

            data_to_write = (f'{hero_id}::{hero_name}::{hero_description}::{hero_comics}::{hero_series}\n')
            usable_file.write(data_to_write)
            numberlist.append(character_to_call)
            #adds this hero to the database for usable characters
        else:
            data_to_write = (f'{hero_name}\n')
            not_usable_file.write(data_to_write)
            #adds this hero to the database for multiple choice

        character_to_call += 1

    numberlist_usable_length = len(numberlist)
    numberlist_not_usable_length = character_to_call - numberlist_usable_length
    numberlist_file.write(str(numberlist_usable_length) + ', ' + str(numberlist_not_usable_length))
    #finds the length of list of usable characters, creating the max value for later calls
    #for both the usable and not usables characters for questions.

    usable_file.close()
    not_usable_file.close()
    numberlist_file.close()


def create_question():
    answer_name, answer_description, answer_comics, answer_series = create_answer()
    wrong_answers = create_multiple_choice()
    full_answer_list = wrong_answers
    full_answer_list.append(answer_name)
    random.shuffle(full_answer_list)

    while True:
        name_to_print = 0
        print(answer_description)
        for i in range(len(full_answer_list)):
            print(f''+str(i+1)+': ' + str(full_answer_list[name_to_print]))
            name_to_print += 1
        print(answer_name)
        user_input = (input('Your answer?: '))

        if user_input == '!hint':
            full_answer_list = hints_system(answer_name, answer_comics, answer_series, wrong_answers)
            print(full_answer_list)
        elif full_answer_list[int(user_input)-1] == answer_name:
            print('Correct!')
            break
        else:
            full_answer_list.remove(full_answer_list[int(user_input)-1])
            print('That was not correct.')


def create_answer():
    usable_file = open('usable_characters_database.txt', 'r')
    numberlist_file = open('usable_numberlist.txt', 'r')
    numberlist_reader = numberlist_file.readlines()
    character_reader = usable_file.readlines()
    #Opens files and creates readers for the files

    number_of_characters = numberlist_reader[0]
    number_of_characters = number_of_characters.split(', ')
    number_of_characters = int(number_of_characters[0])
    #finds the maximum value for the random call

    random_char_int = random.randint(1, number_of_characters)
    character_raw = character_reader[(random_char_int - 1)]
    #index for character file starts at 0, so -1 to the index or it'll search one line ahead of what's actually wanted
    #If changed; could cause bugs

    character_raw = character_raw.split('::')
    character_name = character_raw[1]
    character_description = character_raw[2]
    character_comics = character_raw[3]
    character_series = character_raw[4]
    #takes the raw information from the data and strips it into seperate variables

    character_name = character_name.replace('\n', '')
    character_description = character_description.replace('\n', '')
    character_comics = character_comics.replace('\n', '')
    character_series = character_series.replace('\n', '')
    #Remove /n commands in the files

    character_comics = character_comics.replace('[', '')
    character_comics = character_comics.replace(']', '')
    character_comics = character_comics.split(', ')
    #removes brackets from comics

    character_series = character_series.replace('[', '')
    character_series = character_series.replace(']', '')
    character_series = character_series.split(', ')
    #removes brackets from series

    character_description = utility_commands.filter_description(character_name, character_description)
    #filters name out of the description

    usable_file.close()
    numberlist_file.close()
    return character_name, character_description, character_comics, character_series


def create_multiple_choice():
    not_usable_file = open('not_usable_characters_database.txt', 'r')
    numberlist_file = open('usable_numberlist.txt', 'r')
    numberlist_reader = numberlist_file.readlines()
    character_reader = not_usable_file.readlines()
    #opens files and readers for files

    number_of_characters = numberlist_reader[0]
    number_of_characters = number_of_characters.split(', ')
    number_of_characters = int(number_of_characters[1])
    #finds max value of the list for later calls

    character_list = []
    selected_list = []
    #creates lists

    for i in range(1, 10):
        #input 1, 10 causes 9 names to be selected
        creation_in_use = True
        while creation_in_use:
            random_char_int = random.randint(1, number_of_characters - 1)
            #random integer with the max value of the total list, -1 or index will bug out
            if random_char_int not in selected_list:
                #if character isn't it list already
                character_name = character_reader[random_char_int]
                character_name = character_name.strip()
                selected_list.append(random_char_int)
                creation_in_use = False
                #reads name, strips extras, adds it to variable, breaks loop
                character_list.append(character_name)
                #adds name to list

    not_usable_file.close()
    numberlist_file.close()
    return character_list


def hints_system(right_answer, answer_comic, answer_serie, wrong_answers):
    print('Choose you hint!')
    print('1: 50/50 - removes 50% of the answers')
    print('2: Shows comics the character has been in')
    print('3: Shows series the character has been in')
    choice = input('Which one?: ')
    if choice == '1':
        random.shuffle(wrong_answers)
        new_wrong_answers = []
        for i in range(1, 5):
            new_wrong_answers.append(wrong_answers[i])
        new_wrong_answers.append(right_answer)
        random.shuffle(new_wrong_answers)
        return new_wrong_answers
    if choice == '2':
        line_to_print = 1
        for char in answer_comic:
            print(f'{str(line_to_print)}: {answer_comic}')
            line_to_print += 1
    if choice == '3':
        line_to_print = 0
        for char in answer_serie:
            print(f'{str(line_to_print)}: {answer_serie}')
            line_to_print += 1


