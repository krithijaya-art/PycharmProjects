from colorama import Fore, Style, init
init(strip=False, convert=False)

import json
import sys


# ==========================
# DATA (INTACT AS YOU WANTED)
# ==========================

employees_dictionary = {
    "emp1": {"id": "101", "name": "Balu M", "role": "Project Manager"},
    "emp2": {"id": "102", "name": "Rajan P", "role": "Senior Analyst"},
    "emp3": {"id": "103", "name": "Mathew A", "role": "Validation Engineer"}
}

salary_report = {
    "sal1": {"id": "101", "salary": int(200000)},
    "sal2": {"id": "102", "salary": int(300000)},
    "sal3": {"id": "103", "salary": int(150000)}
}


# ==========================
# MAIN MENU LOGIC
# ==========================

def main():

    id_set = {emp["id"] for emp in employees_dictionary.values()}
    target_id = "201"

    if target_id in id_set:
        print("Employee Ready")
    else:
        print("ID Missing")

    while True:

        print("\nSelect any of the one following categories:")
        print("1. To print the total count:")
        print("2. To list all the entries line by line:")
        print("3. Enter Employee ID to look up the record:")
        print("4. Return the role of the employee if found:")
        print("5. To Add a new record:")
        print("6. To Merge salary report with employee dictionary:")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        # ----------------------------------
        # 1. Total Count
        # ----------------------------------
        if choice == 1:

            if sys.stdout.isatty():
                print(Fore.BLUE +
                      f"Total number of Employees: {len(employees_dictionary)}"
                      + Style.RESET_ALL)
            else:
                print(f"Total number of Employees: {len(employees_dictionary)}")

        # ----------------------------------
        # 2. List All
        # ----------------------------------
        elif choice == 2:

            for key, details in employees_dictionary.items():
                print(Fore.BLUE +
                      f"{details['id']} - {details['name']} ({details['role']})"
                      + Style.RESET_ALL)

        # ----------------------------------
        # 3. Search Employee
        # ----------------------------------
        elif choice == 3:

            record_id = input("Enter Employee ID: ")

            found = False

            for emp, details in employees_dictionary.items():
                if details["id"] == record_id:
                    found = True
                    print("\n" + Fore.GREEN + "Employee found:" + Style.RESET_ALL)
                    print(Fore.BLUE +
                          f"{details['id']} {details['name']} {details['role']}"
                          + Style.RESET_ALL)
                    break

            if not found:
                print(Fore.RED + "Employee not found" + Style.RESET_ALL)

        # ----------------------------------
        # 4. Return Role
        # ----------------------------------
        elif choice == 4:

            def get_role(emp_id, data):
                for details in data.values():
                    if details["id"] == emp_id:
                        return details["role"]
                return "Not Found"

            print(get_role("102", employees_dictionary))
            print(get_role("999", employees_dictionary))

        # ----------------------------------
        # 5. Add New Employee
        # ----------------------------------
        elif choice == 5:

            add_record = input("Enter Employee ID: ")
            add_name = input("Enter Employee Name: ")
            add_role = input("Enter Employee Role: ")

            new_record = "emp" + str(len(employees_dictionary) + 1)

            employees_dictionary[new_record] = {
                "id": add_record,
                "name": add_name,
                "role": add_role
            }

            print("\n" + Fore.GREEN + "Employee added!" + Style.RESET_ALL)

        # ----------------------------------
        # 6. Merge Salary
        # ----------------------------------
        elif choice == 6:

            salary_lookup = {}

            # Step 1: Create lookup
            for sal in salary_report.values():
                salary_lookup[sal["id"]] = sal["salary"]

            # Step 2: Merge
            for emp_details in employees_dictionary.values():
                emp_id = emp_details["id"]

                if emp_id in salary_lookup:
                    emp_details["salary"] = salary_lookup[emp_id]

            print(json.dumps(employees_dictionary, indent=4))

        # ----------------------------------
        # 7. Exit
        # ----------------------------------
        elif choice == 7:
            print("Exiting the Employee dictionary. Have a great day!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


# ==========================
# SAFE FOR PYTEST
# ==========================

if __name__ == "__main__":
    main()
