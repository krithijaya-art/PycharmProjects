employees_dictionary = {
    "emp1": {"id": "101", "name": "Balu M", "role": "Project Manager"},
    "emp2": {"id": "102", "name": "Rajan P", "role": "Senior Analyst"},
    "emp3": {"id": "103", "name": "Mathew A", "role": "Validation Engineer"}
}

salary_report = {
    "sal1": {"id": "101", "salary": 200000},
    "sal2": {"id": "102", "salary": 300000},
    "sal3": {"id": "103", "salary": 150000}
}

def count_employees(data):
    return len(data)

def find_employee(emp_id, data):
    for details in data.values():
        if details["id"] == emp_id:
            return details
    return None

def get_role(emp_id, data):
    for details in data.values():
        if details["id"] == emp_id:
            return details["role"]
    return "Not Found"

def merge_salary(employees_dictionary, salary_report):
    salary_lookup ={}

    for sal in salary_report.values():
        salary_lookup[sal["id"]] = sal["salary"]

    for emp_details in employees_dictionary.values():
        emp_id = emp_details["id"]

        if emp_id in salary_lookup:
            emp_details["salary"] = salary_lookup[emp_id]

    return employees_dictionary
        
