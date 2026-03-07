#!/bin/bash

echo "Running all python projects"

find . -name "*.py" -not -path "*/.venv/*" | while read file
do
	echo "----------------------"
	echo "Running $file"
	python "$file"
done

echo "Execution completed"
