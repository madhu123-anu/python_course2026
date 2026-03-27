# CODING EXERCISE

 #1 using break in while loop
numbers=[25,30,20,40,15,25]
sum=0
i=0
while i<6 :
    sum+=numbers[i]
    if sum>=100:
        print(sum)
        print(f" stop sum exceeds 100 ")
        break   
   
#2 using continue in for loop
for i in range (1,601):
    if i%2==0:
        continue
    else:
        print(i)

#3 using pass in conditional statements
number=int(input("enter a number:"))
if number%2==0:
    print(f"the given number {number} is even")
else:
    pass
    

#4 combining transfer statements
list_words=["hi","skip","hi","hlo","break","why"]
for i in list_words:
    if i =="break":
        break
    elif i=="skip":
        continue
    else:
        print(i)
