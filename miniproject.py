#DICTIONARY OF WORDS
dictionary={}
while True:
    print("1.Add a word")
    print("2.Search for meaning")
    print("3.Display all words")
    print("4.Update meaning")
    print("5.Delete word")
    choice=int(input("enter your choice:"))
    if choice==1:
        word=input("enter the word:")
        meaning=input("enter the meaning:")
        dictionary[word]=meaning
        print(dictionary)
    elif choice==2:
        word=input("enter the word:")
        if word in dictionary:
            print(meaning)
        else:
            print("the word is not included in the dictionary")
    elif choice==3:
        for i in dictionary:
            print(i)
    elif choice==4:
        word=input("enter the word")
        if word  in dictionary:
            new_meaning=input("enter the meaning:")
            dictionary[word]=new_meaning
            print(new_meaning)
    elif choice==5:
        word=input("enter the word")
        dictionary.pop(word)
        print(f"{word} deleted ....")
    else :
        print("invalid choice!!!")
        break
    
        

                
                

    

        

    

