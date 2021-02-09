from random import randint

def pick_a_number():
    result = randint(1,100)
    return result

def ask_for_answer():
    while True:
        user_answer = input("Guess the number: ")
        try:
            user_answer = int(user_answer)
            break
        except ValueError:
            print("It's not a number!")
    return user_answer

computer_picked_number = pick_a_number()
user_picked_number = ask_for_answer()
