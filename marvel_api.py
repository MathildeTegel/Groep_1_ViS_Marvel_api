import time
import hashlib
import json
import random
import utility_commands

database_answers_string = 'quiz_questions.txt'
database_others_string = 'others.txt'
database_settings_string = 'settings.txt'
database_api_keys_string = 'API_keys'


def create_answer():
    usable_file = open(database_answers_string, 'r')
    character_reader = usable_file.readlines()
    numberlist_file = open(database_settings_string, 'r')
    numberlist_reader = numberlist_file.readlines()
    #Opens files and creates readers for the files

    number_of_characters = numberlist_reader[0]
    number_of_characters = number_of_characters.split(', ')
    number_of_characters = int(number_of_characters[0])
    numberlist_file.close()
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

    character_name = utility_commands.format_raw_data(character_name, '1')
    character_description = utility_commands.format_raw_data(character_description, '1')
    character_comics = utility_commands.format_raw_data(character_comics, '2')
    character_series = utility_commands.format_raw_data(character_series, '2')
    character_description = utility_commands.filter_description(character_name, character_description)
    #formats the different kinds of data for later use, filters name out of description.

    usable_file.close()
    numberlist_file.close()

    return character_name, character_description, character_comics, character_series


def create_connection_link(database_offset, apikey):
    api_keys_file = open(database_api_keys_string, 'r')
    api_keys_reader = api_keys_file.readlines()
    url = "http://gateway.marvel.com:80/v1/public/characters"
    timestamp = str(time.time())

    api_data = api_keys_reader[apikey]
    api_data = api_data.replace('\n', '').split('::')
    private_key = api_data[1]
    public_key = api_data[2]
    print(f'Now using API keys with description:{ api_data[0]}')

    hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
    md5digest = str(hash.hexdigest())
    connection_url = f'{url}?limit=1&offset={database_offset}&ts={timestamp}&apikey={public_key}&hash={md5digest}'
    return connection_url


def create_databases():
    answers_file = open(database_answers_string, 'w')
    others_file = open(database_others_string, 'w')
    settings_file = open(database_settings_string, 'w')

    settings_numbers = []
    character_offset = 0
    api_key = 0

    while True:
        hero_comics = []
        hero_series = []
        try:
            connection_url = create_connection_link(character_offset, api_key)
            print(connection_url)
            api_response = requests.get(connection_url)
            jsontext = json.loads(api_response.text)

            hero_id = jsontext['data']['results'][0]['id']
            hero_name = jsontext['data']['results'][0]['name']
            hero_description = jsontext['data']['results'][0]['description']
            hero_description = hero_description.replace('\r', '').replace('\n', '')

            if len(hero_description) > 10:
                for item in jsontext['data']['results'][0]['comics']['items']:
                    hero_comics.append(item['name'])

                for item in jsontext['data']['results'][0]['series']['items']:
                    hero_series.append(item['name'])
                # adds comic and serie information if character has an actual description

                data_to_write = (f'{hero_id}::{hero_name}::{hero_description}::{hero_comics}::{hero_series}\n')
                answers_file.write(data_to_write)
                settings_numbers.append(character_offset)
                # adds this hero to the database for usable characters

            else:
                data_to_write = (f'{hero_name}\n')
                others_file.write(data_to_write)
                # adds this hero to the database for multiple choice

            character_offset += 1
        except ConnectionError:
            print('API is currently not reachable. Please check your internet connection or try again later')
        except KeyError:
            print('API key has been used too many times. Trying next key.')
            api_key += 1
        except IndexError:
            break

    numberlist_usable_length = len(settings_numbers)
    numberlist_not_usable_length = character_offset - numberlist_usable_length
    settings_file.write(f'{numberlist_usable_length}, {numberlist_not_usable_length}')

    answers_file.close()
    others_file.close()
    settings_file.close()


def create_question():
    answer_name, answer_description, answer_comics, answer_series = create_answer()
    wrong_answers = create_wrong_answers()
    full_answer_list = wrong_answers
    full_answer_list.append(answer_name)
    random.shuffle(full_answer_list)

    return answer_name, answer_description, answer_comics, answer_series, full_answer_list

def create_wrong_answers():
    others_file = open(database_others_string, 'r')
    others_reader = others_file.readlines()
    settings_file = open(database_settings_string, 'r')
    settings_reader = settings_file.readlines()

    # opens files and readers for files

    number_of_characters = settings_reader[0]
    settings_file.close()

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
                character_name = others_reader[random_char_int]
                character_name = character_name.strip()
                selected_list.append(random_char_int)
                creation_in_use = False
                #reads name, strips extras, adds it to variable, breaks loop
                character_list.append(character_name)
                #adds name to list

    others_file.close()
    return character_list


