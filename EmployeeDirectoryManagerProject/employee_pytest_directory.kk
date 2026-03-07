from employee_logic import (
    employees_dictionary,
    salary_report,
    count_employees,
    find_employee,
    get_role,
    merge_salary
)

import json
import sys
count = count_employees(employees_dictionary)
print(count)

result = find_employee(emp_id, employees_dictionary)

if result:
    print("Employee found:", result)
else:
    print("Employee not found")

print(get_role("102", employees_dictionary))
print(get_role("999", employees_dictionary))

merged = merge_salary(employees_dictionary, salary_report)
print(merged)

