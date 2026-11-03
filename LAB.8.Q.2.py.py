def display_student_info(**kwargs):
    print("--- Student Information ---")
    if not kwargs:
        print("No information provided.")
        return

    for key, value in kwargs.items():
        # Capitalize and format the key nicely for display
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")


display_student_info(
    name="faseeh",
    age=20,
    major="Computer Science",
    gpa=3.8,
    enrollment_status="Active",
)