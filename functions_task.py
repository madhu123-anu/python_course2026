#CODING EXERCISES
#1.Add function
def add(a,b):
    return a+b
print(add(10,20))

#2.square function
def square(a):
    return a**2
print(square(2))

# #3.factorial function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))

#4.maximum function
my_list=[1,2,3,4,7,9,10]
def maximum():
    return max(my_list)
print(maximum())
maximum()

#5.reverse function
name="preethi singh"
def reverse():
    return name[::-1]
print(reverse())

#6.check prime number
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0 :
            return False
    return True
print(is_prime(4))

#7.palindrome function
name=input("enter name:")
def is_palindrome():
     if name==name[::-1]:
        return True
     return False
print(is_palindrome())

#8.fibanocci function

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(3))

#9.sum of squares
list=[1,2,3,4,5]
def sum_of_squares():
    sum=0
    for i in list:
        result=i**2
        sum+=result
    return sum
print(sum_of_squares())

#10.average function
list=[1,2,3,4,5]
def average():
    result=0
    for i in list:
        result+=i
        ave=result/len(list)
    return ave
print(average())   





