#Find the smallest element in an array

#Find shortest word
word_list = ["Me","Bike","Minnesota","Apple"]

def determine_shortest(list):
    shortestword = min(list, key=len)
    return shortestword

print(determine_shortest(word_list))

#Find the smallest number
numbers = [15,10,100,1]

def smallest_number(list):
    smallnumber = min(list)
    return smallnumber

print(smallest_number(numbers))
