import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from employee_logic import (
    employees_dictionary,
    salary_report,
    count_employees,
    find_employee,
    get_role,
    merge_salary
)

def test_count():
    assert count_employees(employees_dictionary) == 3


def test_find_employee():
    result = find_employee("101", employees_dictionary)
    assert result["name"] == "Balu M"


def test_employee_not_found():
    result = find_employee("999", employees_dictionary)
    assert result is None


def test_get_role():
    assert get_role("102", employees_dictionary) == "Senior Analyst"


def test_role_not_found():
    assert get_role("888", employees_dictionary) == "Not Found"

def test_merge_salary():
    import copy
    from employee_logic import merge_salary, employees_dictionary, salary_report

    # Use copy to avoid modyfying global data
    employees_copy = copy.deepcopy(employees_dictionary)

    merged = merge_salary(employees_copy, salary_report)

    assert merged["emp1"]["salary"] == 200000
    assert merged["emp2"]["salary"] == 300000
    assert merged["emp3"]["salary"] == 150000

    # Also verify salary key exists
    for emp in merged.values():
        assert "salary" in emp
