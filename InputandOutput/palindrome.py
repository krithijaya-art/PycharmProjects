import re  # regular expressions
def is_palindrome(s):
    # Step 1: lowercase
    s = s.lower()

    # Step 2: remove non-alphanumeric characters
    s = re.sub(r'[^a-z0-9]', '', s)

    # Step 3: check palindrome
    return s == s[::-1]

# Take input from user
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("Yes! It's a palindrome.")
else:
    print("No, it's not a palindrome.")