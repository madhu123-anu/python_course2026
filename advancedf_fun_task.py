#CODING EXERCISE
#1.SQUARE_All_NUMBERS
my_list=[1,2,3,4,5]
def square():
    result=map(lambda i:i**2,my_list )
    print(list(result))
square()

#2.FILTER POSTIVE NUMBERS
numbers=[1,4,6,7,-3,-11,-654,7,-45]
def filter_postive_numbers():
    result=filter(lambda i:i>=0,numbers)
    print(list(result))
filter_postive_numbers()

#3.CALCULATE FACTORIAL
from functools import reduce
def calculate_factorial(n):
    fact=1
    result=reduce(lambda a,b,:a*b,range(1,n+1))
    return result 
print(calculate_factorial(3))

#4.COUNT_VOWEL(STRING)
name = input("Enter name: ")
from functools import reduce
def count_vowel():
    result = reduce(lambda count, ch: count + (1 if ch.lower() in "aeiou" else 0), name, 0)
    return result
print(count_vowel())

# filter with 2 iterables # task given in live session
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def fun():
    result1=map(lambda a,b :(a**2,b**2),list1,list2)
    result2=map(lambda a,b :(a+b,b+a),list1,list2)
    print(list(result1))
    print(list(result2))
fun()