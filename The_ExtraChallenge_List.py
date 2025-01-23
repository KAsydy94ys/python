import random
numberList = []
for i in range(5):
    guess = random.randint(1,100)
    numberList.append(guess)
print(numberList)
while True:
    print ("1) Add another number")
    print ("2) Remove a number")
    print ("3) Change a number")
    print ("4) Sum of all numbers")
    print ("5) Print the list, but separate even and odd")
    question = input("Enter your choice: ")
    if question == '1':
        addNumber = int(input("What number do you wanna add then: "))
        numberList.append(addNumber)
        print("This is the the amount of numbers in your list currently:", len(numberList))
        print(numberList)
    if question == '2':
        while True:
            removeNumber = int(input("Enter a number you want to remove mate: "))
            if numberList.__contains__(removeNumber):
                numberList.remove(removeNumber)
                print(numberList)
                break
            else:
                print("The number you want to remove is not in there dumbo")
                continue
    if question == '3':
        while True:    
            editPosition = int(input("Enter the position of the number inside the list: "))
            if editPosition > len(numberList) - 1:
                print ("That position is incorrect")
                continue
            else:
                editNumber = int(input("Enter the new value you want: "))
                numberList[editPosition] = editNumber
                print(numberList)
    elif question == '4':
        boom= sum(numberList)
        print(boom)
    if question == '5':
        evenList = []
        oddList = []
        for i in numberList:
            if i % 2 == 0:
                evenList.append(i)
            else:
                oddList.append(i)
        print ("Even number list:", evenList)
        print ("Odd number list:", oddList)         
