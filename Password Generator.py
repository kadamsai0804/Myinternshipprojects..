import random
import string

def generate_password(length=12):
    """Generate a random password with specified length"""
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))

        # Generate passwords
        passwords = [generate_password(password_length) for _ in range(num_passwords)]

        # Print generated passwords
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)

    except ValueError:
        print("Please enter valid numbers for the number of passwords and password length.")

if __name__ == "__main__":
    main()
