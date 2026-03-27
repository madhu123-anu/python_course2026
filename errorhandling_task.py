#ERROR HANDLING FUNCTIONS

#ValueError
value=int(input("enter value:"))
try:
    print(value)
except:
    print("enter number ")

#TypeError
name="preethi"
value=10 
try:
    print(name+value)
except TypeError as e:
    print("Error:",e)
else:
    print(name)

#FileNotFoundError
file=open("hello.txt",mode='r')
try:
    read_data=file.read()
    print(read_data)
except FileNotFoundError as e:
    print("Error:",e)


#ZeroDivisionError
num_1=int(input("enter num:"))
num_2=int(input("enter num:"))
print(num_1+num_2)
print(num_1*num_2)
try:
    print(num_1/num_2)
    print(num_1%num_2)
except ZeroDivisionError as e:
    print("Error:",e)
else:
    print(num_1**num_2)

#IndexError
list=[1,2,3,4,5,6]
try:
    print(list[8])
except IndexError as e:
    print("Error:",e)

#KEYERROR
dict={"name":"madhu","age":19}
try:
    print(dict("college"))
except KeyError as e:
    print("error",e)

#AttributeError
name="hi"  # example 1
print(name.append("hello"))

class college():  #example 2
    def __init__(self,name,city,district,state):
        self.name=name
        self.city=city
        self.district=district
        self.state=state
try:
    display=college("swr","narsa","wst","ap")
    print(display.age)
    print(display.city)
except AttributeError as e:
    print("Error:",e)
else:
    print(display.district)
    print(display.state)

#OverFlowError
import math #example 1
try:
    print(math.exp(100000))
except OverflowError as e:
    print("Error",e)


num=10 #example 2
try:
    print(int(10**1000000))
except OverflowError as e:
    print("Error",e)

#IOError
file=open("okkk.txt",mode='r')
try:
    read_data=file.read()
    print(read_data)
except IOError as e:
    print("Error",e)

#RunTimeError
y=20
try:
    print(x)
except RuntimeError as e:
    print("Error",e)

#ExceptionError
class college():  #example 1
    def __init__(self,name,city,district,state):
        self.name=name
        self.city=city
        self.district=district
        self.state=state
try:
    display=college("swr","narsa","wst","ap")
    print(display.age)
    print(display.city)
except Exception as e:
    print("Error:",e)
else:
    print(display.district)
    print(display.state)



num=10 #example 2
try:
    print(float(10**1000000))
except Exception as e:
    print("Error",e)