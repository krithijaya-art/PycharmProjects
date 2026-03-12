def generate_test_cases(min_age, max_age):
    return [
        min_age - 1,
        min_age,
        min_age + 1,
        max_age - 1,
        max_age,
        max_age + 1
    ]

tests = generate_test_cases(18, 60)

for t in tests:
    print(f"Testing employee age: {t}")