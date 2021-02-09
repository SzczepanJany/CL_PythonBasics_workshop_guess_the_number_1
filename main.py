from random import randint

def pick_a_number(min_value, max_value ):
    """
    Function is choosing random number from a given range
    """
    result = randint(min_value,max_value)
    return result

def ask_for_answer():
    """
    Function is asking user for an answer and checkin if it is a number 
    """
    while True:
        user_answer = input("Guess the number: ")
        try:
            user_answer = int(user_answer)
            break
        except ValueError:
            print("It's not a number!")
    return user_answer

def check_answer(user_imput, computer_imput):
    """
    Function is comparing user answer with computer picked number
    """
    if user_imput < computer_imput:
        print("To small!")
        return False
    elif user_imput > computer_imput:
        print("To big!")
        return False
    else:
        print("You win!")
        return True


computer_picked_number = pick_a_number(1,100)
win_status = False

while win_status == False:
    user_picked_number = ask_for_answer()
    win_status = check_answer(user_picked_number, computer_picked_number)
