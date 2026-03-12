from sklearn.tree import DecisionTreeClassifier

# experience, skills_score
X = [
    [2, 3],
    [5, 7],
    [8, 9],
    [1, 2]
]

# 1 = hire, 0 = reject
y = [0, 1, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

candidate = [[6, 8]]

prediction = model.predict(candidate)

print("Hire decision:", prediction)