from random import randint

def password_generator():
    how_many = int(input("How many characters do you want in your password [5/128]? "))    
    while how_many < 5 or how_many > 128:
        how_many = int(input("How many characters do you want in your password [5/128]? "))

    characters = user_preferences()

    password = ""

    for i in range(0, how_many):
        password += characters[randint(0, len(characters) - 1)]

    return password
    

def user_preferences():
    """
    Get the user's preferences for the password generator.

    Returns:
        str: A chars set based on the user's preferences.
    """
    low_case = input("Do you want lowercase letters? (y/n) ")
    low_case = test_answer(low_case, "Do you want lowercase letters? (y/n) ")

    up_case = input("Do you want uppercase letters? (y/n) ")
    up_case = test_answer(up_case, "Do you want uppercase letters? (y/n) ")

    num_case = input("Do you want numbers? (y/n) ")
    num_case = test_answer(num_case, "Do you want numbers? (y/n) ")

    sym_case = input("Do you want symbols? (y/n) ")
    sym_case = test_answer(sym_case, "Do you want symbols? (y/n) ")

    return gen_characters(low_case, up_case, num_case, sym_case)


def test_answer(answer, ask):
    """
    Test the answer against a valid set of answers and prompt the user if the answer is invalid.

    Args:
        answer (str): The answer to test.
        ask (str): The question to ask the user if the answer is invalid.

    Returns:
        str: The valid answer.
    """
    while answer.lower() not in ["yes", "no", "y", "n", "not"]:
      answer = input(ask)
      
    return answer


def gen_characters(low_case, up_case, num_case, sym_case):
    """
    Generate the set of characters to use in the password based on the user's answers.

    Args:
        low_case (str): The user's answer for lowercase letters.
        up_case (str): The user's answer for uppercase letters.
        num_case (str): The user's answer for numbers.
        sym_case (str): The user's answer for symbols.

    Returns:
        str: The set of characters to use in the password.
    """
    characters = ""
    options = ["yes", "y",]
    if low_case in options:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if up_case in options:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num_case in options:
        characters += "0123456789"
    if sym_case in options:
        characters += "!@#$%^&*"
        
    return characters


my_password = password_generator()
print(my_password)
