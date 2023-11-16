class Stack():                                                                  # Creates a class to easily handle stack
    def __init__(self):                                                         
        self.items= []                                                          # operations, such as pushing, popping, 

    def isEmpty(self):                                                          # and peeking elements.
        return self.items == []

    def push(self, n):
        return self.items.append(n)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def show(self):
        return self.items

def selection():                                                                # An attempt to reduce code clutter.
    print("""Select stack operation.\n                                          
[C] to create a stack;
[A] to append elements to the stack;
[D] to remove elements from the stack;
[P] to show the top element of the stack;
[S] to show all elements of the stack;
[ANY OTHER KEY] to quit program.\n""")

def nostack():                                                                  # Another attempt to reduce clutter.
    print("\nPlease create a stack first.\n")
    
def yesstack():                                                                 # This function has all of the program's stack operations,
    name = str(input("\nEnter the name of your stack: "))
    stack = Stack()                                                             # which can only be accessed if the user creates a stack.
    print(f"\nStack {name} has been created. Stack elements: {stack.show()}\n")
    while True:                                                                 # If they haven't yet, they will only be prompted to
        selection()
        operation = input("Enter here: ")                                       # create one (through nostack()) before they can proceed.
        match operation:
            case "C" | "c":
                print("\nYou already have a stack.\n")
            case "A" | "a":
                newItem = input("\nPlease insert an element: ")
                stack.push(newItem)
                print(f"\nNew element inserted. Stack {name}'s elements: {stack.show()}\n")
            case "D" | "d":
                stack.pop()
                print(f"\nTopmost element deleted. Stack {name}'s elements: {stack.show()}\n")
            case "P" | "p":
                print(f"\nTopmost element: {stack.peek()}")
                print(f"\nStack {name}'s elements: {stack.show()}\n")
            case "S" | "s":
                print(f"\nShowing stack {name}'s elements: {stack.show()}\n")
            case _:
                print(f"\nDisbanding stack {name} and returning to main program.\n")
                break

while True:                                                                     # This is the main program. If the user has not created a stack
    selection()
    operation = input("Enter here: ")                                           # yet, they will only encounter the nostack() function until
    match operation:
        case "C" | "c":                                                         # they create a stack by pressing the keys 'C' or 'c'.
            yesstack()
        case "A" | "a" | "D" | "d" | "P" | "p" | "S" | "s":
            nostack()
        case _:
            print("\nGoodbye.")
            break
