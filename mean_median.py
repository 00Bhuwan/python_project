# to find mean, median and mode of given list

user_input = input('Enter the numbers: ')
list1 = [int(x) for x in user_input.split()]

def mean():
    mean = sum(list1) / len(list1)
    print(mean)

def median():
    list1.sort()
    n = len(list1)
    if n % 2 == 0:
        m1 = list1[n // 2]
        m2 = list1[n // 2 - 1]
        median = (m1 + m2) / 2
    else:
        median = list1[n // 2]
    print(median)

def mode():
    frequency = {}
    for i in list1:
        frequency.setdefault(i, 0)
        frequency[i] += 1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    print(mode)

mean()
median()
mode()