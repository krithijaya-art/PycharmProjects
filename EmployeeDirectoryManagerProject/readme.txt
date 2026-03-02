You’re helping HR to build a small employee directory. Store basic details in dictionaries, update records, print a clean list, search by ID, and merge data from another department.

Create a dictionary-based tool 
to add/update employees, 
list all entries, 
look up an employee by ID, and 
merge another department’s records.

Questions for this assignment:
Create a base directory with three employees (ID → {name, role}) and print the total count.

Update the role of ID 102 to "Senior Analyst", add a new employee ID 104, then print the directory.

Print a clean roster line by line using a loop: ID - Name (Role).

Write a function get_role(emp_id, data) that returns the role or "Not Found" using if/else (no nesting). Show two calls: one found, one not found.

Merge another department dictionary into employees and print the merged result.

Decision check: set target_id = 201. If the ID exists, print "Employee Ready", else print "ID Missing".