employees = []

for i in range(3):
    print("Employee", i + 1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    employees.append((name, age, salary))

print("Employee list:")
for emp in employees:
    print(emp)