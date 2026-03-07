#This is for getting input from user
name = input("What is your name?")
#Ask for age if the name is not empty
if name != "":
    valid_name = True  # assume name is valid initially
    for char in name:
        if not (char.isalpha() or char == " "):
            valid_name = False
            break  # stop checking if any invalid character is found
    if valid_name:
        age = input("Please enter your age: ")
        # Step 5: Check if age is a number
        if age == "" or not age.isdigit():
            print("Enter a valid age.")
        else:
            print("Welcome", name)
    else:
        print("Invalid name. Please use only letters and spaces.")
else:
    print("Name cannot be empty.")