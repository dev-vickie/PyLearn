stack = []
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)
    
def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        e = stack.pop()
        print("Removed element: ",e)
        print(stack)

while True:
    print("select operation: \n1.Push\n2.Pop\n3.Quit\n ::")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the right operation here")