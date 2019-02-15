#Find the largest element in an array

#Find longest word
word_list = ["Me","Bike","Minnesota","Apple"]

def determine_longest(list):
    longestword = max(list, key=len)
    return longestword

print(determine_longest(word_list))

#Find the biggest number
numbers = [15,10,100,1]

def biggest_number(list):
    bignumber = max(list)
    return bignumber

print(biggest_number(numbers))
