import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    password = ''.join(password)
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length for your password (minimum 8 characters): "))
    
    if length < 8:
        print("Password length should be at least 8 characters.")
        return
    
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
