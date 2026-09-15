name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

subjects = ["English", "Math", "Physics", "Chemistry", "Computer"]
marks = []
failed = False

# Input marks for each subject
for sub in subjects:
    score = float(input(f"Enter marks for {sub}: "))
    marks.append(score)
    if score < 40:
        failed = True

total = sum(marks)
percentage = (total / 500) * 100

# Determine Grade
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Result check
if failed or percentage < 40:
    result = "Fail"
else:
    result = "Pass"

# Print Marksheet
print("\n--- MARKSHEET ---")
print("Name:", name)
print("Roll No:", roll)
print("-----------------")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")
print("-----------------")
print("Total:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)