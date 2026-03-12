While containerizing the AI testing project using Docker, the PyTorch dependency download failed due to network timeout because the package size is very large (~900 MB). I resolved it by installing the CPU-optimized PyTorch wheel from the official repository and adjusting pip installation settings to make the build reliable for CI pipelines

This ai_anomaly_detection module demonstrates how AI can assist testing of HR datasets. I used a small neural network built with PyTorch. The model takes salary and years of experience as inputs and learns the normal patterns in the data. During training, the model minimizes the error using mean squared loss and an Adam optimizer. Once trained, it can be used to flag abnormal HR records such as unusually high salaries for low experience.

Here a model dataset is used, but in real time systems, the HR data is stored in systems like SAP SuccessFactors, Workday, Oracle HCM. These systems store data in databases.

Example tables are:
  Employees
  Payroll
  Compensation
  Performance
  Attendance

| employee_id | role     | salary | experience_years | department | bonus |
| ----------- | -------- | ------ | ---------------- | ---------- | ----- |
| 101         | Engineer | 70000  | 5                | IT         | 5000  |
| 102         | Manager  | 120000 | 10               | HR         | 12000 |
| 103         | Engineer | 60000  | 3                | IT         | 4000  |

From this dataset the AI learns patterns such as:

salary vs experience
salary vs role
bonus vs salary

This data is exported from HR systems as CSV or database queries.

salary,experience
50000,2
70000,5
90000,8
60000,3
120000,10

Then in python:-

import pandas as pd
import torch

# load historical HR data
df = pd.read_csv("hr_salary_data.csv")

data = torch.tensor(df.values, dtype=torch.float)

This replaces the hardcoded dataset.
The columns are chosen based on business relevance

Feature selection :-

| Feature           | Reason                     |
| ----------------- | -------------------------- |
| salary            | detect abnormal pay        |
| experience        | salary correlation         |
| department        | department pay differences |
| bonus             | detect payroll mistakes    |
| performance score | unusual compensation       |

“In a real HR system the historical data would be extracted from the HR database or payroll system as CSV or database queries. Features such as salary, experience, department and bonus would be selected based on HR domain knowledge. That dataset would then be used to train the anomaly detection model.”

Finally this project demonstrates four valuable skills together:

Python programming

PyTorch AI model

pytest automated testing

Docker container execution
