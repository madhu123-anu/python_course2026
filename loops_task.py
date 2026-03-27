  #CODING EXERCISE
 #1 sum of sqares
sum=0
for i in range(1,6):
    squares=i**2
    print(squares)
    sum +=squares
    print(sum)

 #2 countdown
countdown=int(input("enter value"))
while countdown>=1:
    countdown-=1
print(countdown)
    
 #3 multiplication table with nested for
number=int(input("enter a value:"))
for i in range(1,2):
     for j in range(1,11):
        print(f"{number}x{j}={number*j}")

#4 program using for loop to find sum of all even numbers btw 0 to 10
sum = 0
for numbers in range(0,11):
    if numbers%2==0:
         print(numbers)
         sum+=numbers
print(F"sum of all even numbers ranges from 0 to 11 is {sum}")
    
 #5 sum of all numbers from 1 to a given number
sum = 1
number=int(input("enter a number:"))
for i in range(1,number+1):
    sum+=i
    print(sum)

#6 display numbers from a list
number_list=[1,2,3,4,25,40,50,60]
for i in number_list:
    print(i)

 #7 display numbers from -10 to -1
for i in range(-10,0):
     print(i)

 #8 cubes of all numbers from 1 to agiven number
number=int(input("enter a number:"))
for i in range(1,number+1):
     print(i**3)
