#Find the missing element

numbers = [0,1,2,4,5,6,7,8,9]

def number_check(list):
    correct_list = [0,1,2,3,4,5,6,7,8,9]
    missingnumber = []
    for index in correct_list:
        if index not in list:
            missingnumber.append(index)
    return missingnumber

print(number_check(numbers))
