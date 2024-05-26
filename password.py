import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("The length should be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
