#without hiding 

database = {}

def add():
    while True:
        key = input('Enter the username(or type "stop" to finish): ')
        if key.lower() == 'stop':
            break
        value = input('Enter password: ')
        database[key] = value

    print('Following are the username and password: ', database)

def verify():
    while True:
        username = input('Enter the username: ')
        if username in database.keys():
            password = input('Enter the password: ')
            while password != database[username]:
                password = input('Incorrect password. Enter the password again: ')
            print('verified!!!')
            break
        else:
            print('Username Incorrect!!')

add()
verify()