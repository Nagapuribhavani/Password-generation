import string
import random

def generate_password(length, complexity):
    characters = ''
    if '1' in complexity:
        characters += string.ascii_lowercase
    if '2' in complexity:
        characters += string.ascii_uppercase
    if '3' in complexity:
        characters += string.digits
    if '4' in complexity:
        characters += string.punctuation
    
    if not characters:
        print("No complexity level selected. Please choose at least one complexity level.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    
    # Input password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length should be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for length.")
        return
    
    # Input password complexity
    print("Select complexity level (you can combine multiple levels):")
    print("1. Lowercase letters")
    print("2. Uppercase letters")
    print("3. Digits")
    print("4. Special characters")
    
    complexity = input("Enter the complexity level (e.g., '123' for lowercase, uppercase, and digits): ")
    
    password = generate_password(length, complexity)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()
