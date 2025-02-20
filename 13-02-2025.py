
def orderString():
    string = input("Enter a word, use uppercase and lowercase pleaseee: ")
    array_uppers = []
    array_lowers = []
    for c in string:
        if c != ' ':
            if c.isupper():
                array_uppers.append(c)
            else:
                array_lowers.append(c)
    thefinale = array_lowers, array_uppers
    string_upper = ''.join(array_uppers)
    string_lower = ''.join(array_lowers)
    text = string_lower+string_upper.lstrip(' ')
    print (text)

def positioningFirstMiddleLast():
    string = input("Enter a word: ")
    first_chac = string[0]
    print (first_chac)
    middlelength = len(string)
    middle = middlelength // 2
    completor = string[middle]
    print(string[middle])
    last_pos = len(string) - 1
    last_chac = string[last_pos]
    print (last_chac)
    finale = (first_chac, completor, last_chac)
    joined =   ''.join(finale)
    print(joined)

def antiVowel():
    vowels = ['a','e','i','o','u']
    detector = input("Enter a word: ")
    for c in detector:
        if c in vowels:
            detector = detector.replace(c, '')
    print(detector)

while True:
    print ("To activate orderString, type 1")
    print ("To activate positioningFirstMiddleLast, type 2")
    print ("To activate antiVowel, type 3")
    print ("To stop the code, press n")
    option_choice = input("Enter your choice: ")
    if option_choice == '1':
        orderString()
    elif option_choice == '2':
        positioningFirstMiddleLast()
    elif option_choice == '3':
        antiVowel()
    elif option_choice == 'n':
        break
    else:
        print("That is not an option, try again")

