'''
AI-assisted anomaly detection for HR datasets.

Purpose:
This module demonstrates how an AI model can be used to detect anomalies
in HR data such as abnormal salary entries or inconsistent employee records.

Technology used:
PyTorch to simulate automated validation of payroll data.
'''

# Import required libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

# --------------------------------
# Step 1: Create Sample HR dataset
# --------------------------------
# Each row represents an employee record
# features: [salary, experience_years]
# data = torch.tensor([
#    [50000, 2],
#    [70000, 5],
#    [90000, 8],
#    [60000, 3],
#    [120000, 10]
# ], dtype=torch.float)

# -------------------------------------
# Step 1: Load Historical HR dataset
# -------------------------------------
df = pd.read_csv("hr_data.csv")

# convert to tensor for AI model
data = torch.tensor(df.values, dtype=torch.float)

# --------------------------------------
# Step 2: Define a simple neural network
# --------------------------------------
# Input layer size = 2 (salary, experience)
# Hidden layer = 4 neurons
# Output layer = 1 value (anamoly score)

model = nn.Sequential(
    nn.Linear(2, 4),    # transforms input features to hidden layer
    nn.ReLU(),          # activation function
    nn.Linear(4, 1)     # finaly output layer
)

# ------------------------------
# Step 3: Define optimiser and loss
# ------------------------------
# optimizer adjusts model weights during training
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Loss function measures prediction error
loss_fn = nn.MSELoss()

# ---------------------------------
# Step 4: Define training targets
# ---------------------------------
# In this example we assume all records are normal (no anamoly)
# so the expected output is 0

target = torch.tensor([[0],[0],[0],[0],[0]], dtype=torch.float)

# --------------------------
# Step 5: Train the AI model
# ---------------------------
# The model learns patterns in HR data

for epoch in range(100):
    # Model predicts anomaly score
    prediction = model(data)

    # Calculate difference between prediction and expected output
    loss = loss_fn(prediction, target)

    # Reset gradients
    optimizer.zero_grad()

    # Backpropagation (learn from errors)
    loss.backward()

    # Update model weights
    optimizer.step()

# --------------------------
# Step 6: Training completed
# --------------------------
print("Model trained to detect anomalies")
