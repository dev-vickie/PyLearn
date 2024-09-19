import random

def guess(x):
    # gen a random number
    random_number = random.randint(1,x)

    guess = 0
    while guess != random_number: 
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry,thats too low")
        elif guess > random_number:
            print("Sorry,thats too high")
    print(f"You have got it - {random_number}")
        

def computer_guess(x):
    low = 1
    high = x
    

guess(10)

