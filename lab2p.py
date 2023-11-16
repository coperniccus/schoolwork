# Array 1 : Create a program that could determine how many
# array larger number than 10 are inputted by the users.

def ArrayBuilder():
    import array as arr
    arr = []
    
    print("\nBuild an array of 10 numbers. Enter your chosen numbers below.\n")
    
    for i in range(10):                                                         # For loop to repeatedly take inputs
        elements = int(input(f"Number #{i+1}: "))                               # and place them into the array.
        arr.append(elements)
        arrOverTen = []
        for i in arr:
            if i > 10:
                    arrOverTen.append(i)
            else:
                pass
    
    print(f"""\nNumbers larger than 10: {arrOverTen}
    \nYou have entered {len(arrOverTen)} numbers larger than 10.
    \nReturning to main program...""")
    
# Array 2:  Create a program that will determine if the string
# inputted by end -user is a palindrome or not.

def PalindromeChecker():
    print("\nEnter your word below, and find out if it's a palindrome or not.\n")
    
    userinput = input("Word: ")
    
    inputChr = list(userinput)                                                  # List() and reversed() methods were used for
    inputChrRev = list(reversed(userinput))                                     # convenience.
    
    print(inputChr)
    print(inputChrRev)
    
    if inputChr == inputChrRev:
        print("\nYour word is a palindrome. \nReturning to main program...")
    else:
        print("\nYour word is not a palindrome. \nReturning to main program...")
    
# Array 3: Detect an input value value given by the end-user, if the user press
# 1 it will continuously asked end-user to input an integer value, if the user 
# press 0 it display all the input values and its corresponding element number.     

def ListBuilder():
    import array as arr
    
    arr = []
    
    while True:
        takeInput = input("""Press [1] to enter an element. 
Press [0] to display all inputted values and return to main program.
Press any other key to return to main program.\n""")
        
        match takeInput:                                                        # Flow control to dictate the program's actions
            case "1":                                                           # depending on user input.
                element = input("\nEnter element: ")
                arr.append(element)
            case "0":
                for i in arr:                                                   # This section will display every inputted value
                    print(f"Element {arr.index(i)}: {i}")                       # and the element number.
                    print("\nReturning to main program...")
                break
            case _:
                print("\nReturning to main program...")
                break
   
while True:                                                                     # Main program is looped for convenience.
    task = input("""\nWhat would you like to open?
[1] Array-builder;
[2] PalindromeChecker;
[3] List-builder;
[ANY OTHER KEY] Quit.
 
Enter here: """)
 
    match task:                                                                 # This section will allow the user to choose which
        case "1":                                                               # program to operate by inputting their choices
            ArrayBuilder()                                                      # and putting their input into flow control. The
        case "2":                                                               # loop is broken and the main program is exited if
            PalindromeChecker()                                                 # the user inputs a key not included in the valid
        case "3":                                                               # choices.
            ListBuilder()
        case _:
            print("Goodbye.")
            break
        
        
        
        
        
        
        
        

