#TASK
#1.intersection [exercise 1]
set1={1,2,3,4,5}
set2={4,5,6,7,8}
result=set1.intersection(set2)
print(result)

#2.union [exercise 2]
set1={1,2,3,4,5}
set2={4,5,6,7,8}
result=set1.union(set2)
print(result)

#3.set difference [exercise 3]
set1={1,2,3,4,5}
set2={4,5,6,7,8}
result=set1.difference(set2)
print(result)

#4.symmetric difference [exercise 4]
set1={1,2,3,4,5}
set2={4,5,6,7,8}
result=set1.symmetric_difference(set2)
print(result)

#5.membership test
my_set={1,2,3,4,5}
for i in my_set:
    if i==3:
        print("True")

