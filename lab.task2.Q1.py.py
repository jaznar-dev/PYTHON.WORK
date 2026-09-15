hours = float(input("enter hours: "))
rate = float(input("enter rate: "))

if hours <= 35:
    total_pay = hours * rate
    print(f"Total pay (No overtime): ${total_pay:.2f}")

else:
    overtime_hours = hours - 35
    regular_pay = 35 * rate
    overtime_pay = overtime_hours * rate * 1.5
    total_pay = regular_pay + overtime_pay

    print(f"Regular pay: ${regular_pay:.2f}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Total pay: ${total_pay:.2f}")
