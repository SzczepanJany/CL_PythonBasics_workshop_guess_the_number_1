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

def check_answer(user_imput, computer_imput):
    if user_imput < computer_imput:
        print("To small")
        return False
    elif user_imput > computer_imput:
        print("To big")
        return False
    else:
        return True


computer_picked_number = pick_a_number()
win_status = False

while win_status == False:
    user_picked_number = ask_for_answer()
    win_status = check_answer(user_picked_number, computer_picked_number)
