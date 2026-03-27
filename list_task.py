#TASK1
# reverse list
my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)

#TASK2
# common elements
print([i for i in [1,2,3,4,5] for j in [4,5,6,7,8] if i==j])

#TASK3
# unique elements
unique_list=[]
original_list=[1,2,2,3,4,4,5]
for i in original_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

#TASK4
# remove duplicates
duplicate_list=[1,2,2,3,4,4,5]
empty_list=[]
for i in duplicate_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)

# list concantenation
list_1=[1,2,3]
list_2=[4,5,6]
list_1.extend(list_2)
print(list_1)

#list removal
list=[1,2,3,4,5,6,7,8,9]
newlist=list[0::2]
print(newlist)

#list repetation
list=[1,2,3]
repeat=[list]*3
print(repeat)

#list insertion
list=[1,2,3,4,5,6,7,8,9]
list.insert(0,10)
list.insert(1,11)
list.insert(2,12)
print(list)
list.sort()
print(list)

# TASK5
#LIST COMPHREHENSIONS

#square numbers
print([i**2 for i in range(1,11)])

#even numbers
print([i for i in range(1,21) if i%2==0])

#words length
print([len(i) for i in ["apple","banana","cherry","date"] ])