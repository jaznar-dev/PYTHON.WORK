def display_employee_info(**kwargs):
    print("--- Employee Information ---")
    if not kwargs:
        print("No information provided.")
        return

    for key, value in kwargs.items():

        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")



display_employee_info(
    name="Jane Doe",
    position="Senior Developer",
    department="Engineering",
    salary=115000,
    remote=True,
)