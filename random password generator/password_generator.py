import random
import string
import pyperclip  # You may need to install this using: pip install pyperclip

# Function to generate a random password based on user criteria
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase  # Add uppercase letters if selected
    if use_numbers:
        characters += string.digits  # Add digits if selected
    if use_symbols:
        characters += string.punctuation  # Add symbols if selected
    
    if not characters:
        return "No valid character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard!")

# Main function to interact with the user
def main():
    print("Welcome to the Secure Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"Generated Password: {password}")

    # Ask if the user wants to copy it to the clipboard
    copy = input("Do you want to copy the password to the clipboard? (y/n): ").lower() == 'y'
    if copy:
        copy_to_clipboard(password)

if __name__ == "__main__":
    main()

