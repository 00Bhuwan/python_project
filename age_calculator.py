import datetime as dt

def age_calculator():
    year = int(input('Enter your birthyear: '))
    month = int(input('Enter your birthmonth: '))
    day = int(input('Enter your birthday: '))
    today = dt.datetime.now().date()
    dob = dt.date(year, month, day)
    age = int((today - dob).days / 365)
    print(f'you are {age} years old.')
    
age_calculator()