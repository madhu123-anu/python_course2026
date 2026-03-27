#CODING EXERCISE
#1.creates a tuple
my_tuple=("name","john","age",25,"color","white")
print(my_tuple)

#2.access a tuple
my_tuple=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(my_tuple[3])

#3.tuple concatenation
my_tuple1=("preethi")
my_tuple2=("singh")
print(my_tuple1 + my_tuple2)

#4.tuple unpacking
rectangle=(10,20)
length,width=rectangle
area=length*width
print(length)
print(width)
print(area)

#5.checks if an element exists
my_tuple=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
if "tuesday" in my_tuple:
        print(True)

#6. to generate bill for a supermarket purchase
items=[("apple",99),("banana",99),("milk",49)]
print("Item\tPrice")
print("-"*18)
total=0
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
print("-"*18)
print(f"total\t{total}")

