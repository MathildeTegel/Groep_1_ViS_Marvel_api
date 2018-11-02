import marvel_api_calls

print('Welcome to the Marvel Quiz!')

while True:
    print('1: Load database')
    print('2: Play game')
    print('3: Exit game')
    print('4: Test function')
    user_answer = input('Enter Command: ')
    if user_answer == '1':
        marvel_api_calls.create_databases()
    elif user_answer == '2':
        marvel_api_calls.create_question()
    elif user_answer == '3':
        break
    elif user_answer == '4':
        import utility_commands
        info = open('usable_characters_database.txt', 'r')
        reader = info.readlines()
        index = 230
        while index != 235:
            character_raw = reader[index]
            index += 1
            print(str(character_raw))


