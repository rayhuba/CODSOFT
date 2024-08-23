#To generate random characters, you'll need the random module, which is part of Python's standard library.
import random
#Iused the string module to access different sets of characters (letters, digits, and punctuation).
import string


#Get the User input for Password Length
def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length:"))
            if length > 0:
                return length
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input.Please enter a number")

#Generate a Random Password
def generate_password(length):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(random.choice(characters)for i in range(length))
    return password

#Display the Generated Password
def display_password(password):
    print(f"Your generated password is:{password}")

#Putting it all together
def main():
    length = get_password_length()
    password = generate_password(length)
    display_password(password)

if __name__== "__main__":
    main()