def find_missing_number(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

list = input('enter a list of numbers: ')
list1 = [int(x) for x in list.split()]
print(list1)
print(find_missing_number(list1))