pwd = input('Master password: ')

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user


def add():
    name = input("username: ")
    password = input('password: ')
    with open('password.txt', 'a') as f:
        f.write(name + '| ' + password + '\n')
        
mode = input('Type view to view existing password and add to add a new password. Press q to quit: ').lower()
while True:
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Enter valid operation to be performed!!")
        continue
