import random

var = [
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
93, 94, 95, 96, 97, 98, 99, 100
]

random.shuffle(var)

print("From 1 - 100, i chose a number. Guess it correctly")
level = input("Choose a difficulty: easy or hard?: ")
vary = random.choice(var)
rule = 8
guess = 0

def funcname():
    if attempt < vary:
        print("You guessed too low\nGuess  again!")
    if attempt > vary:
        print("You guessed too high\nGuess again!")

if level == "easy":
    comp = False
    print("You have 8 attempts: ")
    while not comp:
        attempt = int(input("\nMake a guess: "))
        funcname()
        if attempt == vary:
            print("You correct")
            comp = True
            break
        guess += 1
        rule -= 1
        print(f"You have {rule} more attempts.")
        if guess == 8 :
            comp = True
            break
elif level == "hard":
    rule -= 3
    comp = False
    print("You have 5 attempts: ")
    while not comp:
        attempt = int(input("Make a guess: "))
        funcname()
        if attempt == vary:
            print("You correct")
            comp = True
            break
        guess += 1
        rule -= 1
        print(f"You have {rule} more attempts.")
        if guess == 5:
            comp = True
            break