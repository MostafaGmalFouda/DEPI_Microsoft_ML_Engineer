import random
def generate_random_string(number:int = 4):
    """
    this function to generate password depend on number of characters that user choose

    :parem_1 : take number of characters from input user interface
    type parem_1 : int
    
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for i in range(number):
        password += random.choice(characters)
    return f"Genrated password : {password}"

        