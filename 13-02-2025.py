def findFactors():
    factors = []
    divisor = int(input("Enter a number: "))
    print ("The factors of that number is: ")
    for i in range(1, divisor + 1):
        if divisor % i == 0:
            factors.append(i)
    print (factors)

def hangman():
    word = "qewrtyuioafsfkfl"
    array_inside = []
    while True:
        letter = input("Enter a letter or the word: ")
        if letter in word:
            print("true")
        else:
            print("false")

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

art = """
 _______  _______  ______   _______    _______  _______  _        _        _______  _______ __________________ _______  _       
(  ____ \(  ___  )(  __  \ (  ____ \  (  ____ \(  ___  )( \      ( \      (  ____ \(  ____ \\__   __/\__   __/(  ___  )( (    /|
| (    \/| (   ) || (  \  )| (    \/  | (    \/| (   ) || (      | (      | (    \/| (    \/   ) (      ) (   | (   ) ||  \  ( |
| |      | |   | || |   ) || (__      | |      | |   | || |      | |      | (__    | |         | |      | |   | |   | ||   \ | |
| |      | |   | || |   | ||  __)     | |      | |   | || |      | |      |  __)   | |         | |      | |   | |   | || (\ \) |
| |      | |   | || |   ) || (        | |      | |   | || |      | |      | (      | |         | |      | |   | |   | || | \   |
| (____/\| (___) || (__/  )| (____/\  | (____/\| (___) || (____/\| (____/\| (____/\| (____/\   | |   ___) (___| (___) || )  \  |
(_______/(_______)(______/ (_______/  (_______/(_______)(_______/(_______/(_______/(_______/   )_(   \_______/(_______)|/    )_)
"""


while True:
    print(art)
    print ("To order strings from lower case to uppercase, type 1")
    print ("To take only the first middle and last letter from a string, type 2")
    print ("To activate antiVowel, type 3")
    print ("To find divisors of an interger, type 4")
    print ("To play hangman, type 5")
    print ("To stop the code, press n")
    option_choice = input("Enter your choice: ")
    if option_choice == '1':
        orderString()
    elif option_choice == '2':
        positioningFirstMiddleLast()
    elif option_choice == '3':
        antiVowel()
    elif option_choice == '4':
        findFactors()
    elif option_choice == '5':
        hangman()
    elif option_choice == 'n':
        break
    else:
        print("That is not an option, try again")




