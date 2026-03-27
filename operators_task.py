#CODING EXERCISE
#1 create a program that takes user input for their name and age
name=input("enter name:")
age=input("eneter age:")
print(f"The user name is {name} and age is{age}")


#2 create a list and check the numbers in a list
numbers_list=[1,2,3,4,5,6,7,8,9,10]
print(5 in numbers_list)
print(15ha not in  numbers_list) 


#TASK
#1 calculate the area of the rectangle
length=int(input("enter length:"))
width=int(input("enter width:"))
area=length*width
print(f"Area of the rectangle is {area} when length={length}and width={width}")


#2 incrementing and decrementing a variable
height=float(input("enter height:"))
height+=5 # compound assignment height=height+5
print(height)
height2=float(input("enter height2:"))
height2-=5# height2=height2-5
print(height2)


#3 convert tenperature from celsius to fahrenheit
celsius_temp=int(input("enter temperature:"))
fahrenheit=(celsius_temp*9/5)+32
print(fahrenheit)


#4 calculate the simple interest
amount=int(input("enter amount:"))
rate=int(input("enter interest rate:"))
time=int(input("enter time in years:"))
simple_interest=(amount*rate*time)/100 # formulae ptr/100
print(simple_interest)


#5 concatenate 2 strings
name_1=input("enter name_1:")
name2_=input("enter name_2:")
print("conatenated strings is:",name_1+name2_)


#6 convert distance from kilometer to miles
distance_kilo=int(input("enter distance:"))
print(distance_kilo)
distance_kilo*=0.621
miles=distance_kilo
print(f"converted distance from kilometers to {miles} miles")


