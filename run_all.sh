#!/bin/bash

echo "Running all python CLI programs"
echo "-------------------------------"

find . -name "*.py" -not -path "*/.venv/*" -not -path "*/tests/*" | while read file
do
    if grep -q "__main__" "$file"; then
        echo "Running $file"

        dir=$(dirname "$file")

        # If input file exists, use it
        if [ -f "$dir/employee_input.dat" ]; then
            python "$file" < "$dir/employee_input.dat"
        else
            python "$file"
        fi

        echo "-------------------------------"
    fi
done

echo "Running pytest"
pytest -v

echo "Execution completed"
