import random
import string

def password_generator():
    while True:
       try:
        a = int(input("Enter the length of the password: "))
        break
       except ValueError:
            print("Please enter a valid integer.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(a))
    return password


print(password_generator())