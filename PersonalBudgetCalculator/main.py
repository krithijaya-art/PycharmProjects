# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Personal Budget Calculator

    #Get income from the user
    income = int(input("Enter your total monthly income: "))

    #Get expenses from the user
    rent = int(input("Enter your total monthly rent: "))
    groceries = int(input("Enter your total monthly groceries: "))
    transport = int(input("Enter your total monthly transportation: "))
    utilities = int(input("Enter your total monthly utilities: "))
    other_expenses = int(input("Enter your other expenses: "))

    #calculate the total expense
    total_expenses = rent + groceries + transport + utilities

    #calculate remaining budget
    remaining_budget = income - total_expenses

    #display the result
    print("Total income:", income)
    print("Total expenses:", total_expenses)
    print("Remaining budget:", remaining_budget)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
