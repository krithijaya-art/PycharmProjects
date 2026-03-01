n = input("Enter a number to sum its digits: ")
if not n.isdigit():
    print("Error:please enter a valid number")
elif int(n) < 10:
    print("Error: Number must be 10 or greater to have a 2-digit sum!")
else:
    s = sum(int(d) for d in n)
    print(f"The sum of the digits is {s}")