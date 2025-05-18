def greeting():
    print("Hello! My name is Aid.")
    print("I was created in 2025.")

def remind_name():
    print("Please, remind me your name. ")
    name = str(input())
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3= int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())
    i = 0
    while i <= num:
        print(f"{i} !")
        i += 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    user_answer = int(input())
    if user_answer == 2:
        print("Congratulations, have a nice day!")
    else:
        print("Please try again")
        while True:
            user_answer = int(input())
            if user_answer == 2:
                print("Congratulations, have a nice day!")
                break
            print("Please try again")
greeting()
remind_name()
guess_age()
count()
test()



