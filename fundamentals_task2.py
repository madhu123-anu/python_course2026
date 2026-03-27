#CODING EXERCISES
1.#print statement
print("My name is Madhuri")#o/p My name is Madhuri
#comments
2.#explaing the single and multiple line comments
'''
comments==>comments are used to explain the code
single line comments==>which are used to write the brief code
multi line comments==>which are used to write the large discriptive
'''
#data structures & datatypes
sample_list=[20,3.5,(2,'alice',3.5),"bob"]
print(sample_list)#o/p [20, 3.5, (2, 'alice', 3.5), 'bob']
employee_id={101,102,103}
print(type(employee_id))#<class 'set'>
#string operations
name1="hari"
name2="ramu"
print(name1+name2)#hariramu
print(name1*3)#hariharihari
#python keywords
'''
if=5 #here we taken python keyword int as variable
print(if)#showing an error because keywords have predefined meaning'''

#type conversions
num1 = 3.6
print(type(num1))#<class 'float'>
print(int(num1))#3
print(type(int(num1)))#<class 'int'>

num2=4#int==>string
print(type(num2))#<class 'int'>
print(str(num2))#4
print(type(str(num2)))#<class 'str'>
#input&output
age=input("enter age:")#30
print(age)#o/p 30

#EXERCISE
#1.print statement
print('@')
print('@@')
print('@@@')
print('@@@@')
print('@@@@@')
#2.comments
#performing multiplication of 2 numbers
num1=2
num2=3
print(num1*num2)#o/p 6
'''
here num1 stores the value of 2
num 2 stores the value of 3
in print statement it performs multiplication of 2 numbers and display the output 
'''
#3.data structures and datatypes
sample_dict={"title":"Rainbow","author":"surender","publicationyear":2001}
print(sample_dict)# o/p {'title': 'Rainbow', 'author': 'surender', 'publicationyear': 2001}
print(type(sample_dict))#<class 'dict'>
#4.string operations
product_price=input("enter price:")# 400
print(product_price)# 400
print(type(product_price))
print(float(product_price))#400.0
print(type(float(product_price)))#{'title': 'Rainbow', 'author': 'surender', 'publicationyear': 2001}
#5.concatenate strings
name1="raghu"
name2="ram"
print(name1+name2)# o/p raghuram
#6.type conversion
age=input("enter age:")#20
conversion=int(age)
print(type(conversion))#int
print(conversion+5)#o/p 25

#7.input and output
num1=2
num2=3
print(num1*num2)#o/p 6
