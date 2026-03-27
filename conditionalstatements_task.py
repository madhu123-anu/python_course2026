#EXERCISE

#1.vowel checker
vowels=input("enter vowels:")
if vowels in "aeiouAEIOU":
    print("vowels")
else:
    print("consonants")

#2.age group classification
age=int(input("enter age:"))
if age>=0 and age<=12:
    print("the person belongs to child")
elif age>=13 and age<=17:
    print("the person belongs to teenager")
elif age>=18 and age<=64:
    print("the person belongs to adult")
else:
    print("the person belongs to older")
    
#3.number classifier
number=int(input("enter number:"))
if number==0:
    print("the given number is zero")
elif number>0:
    print("the given numbers are positive")
else:
    print("the given numbers are negative")

#4.leap year
leap_year=int(input("enter year:"))
if (leap_year%4==0 or leap_year%400==0) and (leap_year%100!=0):
    print("leap year")
else:
    print("not a leap year")
#5.calculator
num_1=int(input("enter num_1:"))
num_2=int(input("enter num_2:"))
operator=input("enter operator:")
if operator=='+':
    print("perform addition",num_1+num_2)
elif operator=='-':
    print("perform subtraction",num_1-num_2)
elif operator=='*':
    print("perform multiplication",num_1*num_2)
else:
    print("perform division",num_1/num_2)

#6.short hand if
num=int(input("enter num:"))
print("even") if num%2==0 else print("odd")

#7.discount calculator
original_price=int(input("enter price:"))
discount_perc=int(input("enter discount:"))
discount=original_price*(discount_perc)/100
final_price=original_price-discount
print(final_price)

#8.BMI calculator
weight=float(input("enter weight:"))
height=float(input("enter height:"))
bmi=weight/height**2
print(bmi)
