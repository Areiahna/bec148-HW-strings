# Task 1: Input Length Validator 
    # Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

def user_name():
    while True:
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")

            if (len(first_name) < 2 ) or (len(last_name) <2):
                print("Name must be at least 2 characters long!")
                print("=" *25)
                continue

        except ValueError:
            print("Dude really?")

        else:
            print("=" *25)
            return print(f"Hello, {first_name} {last_name}!")
        

user_name()
