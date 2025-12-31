def average_calculator(total, count):
    return round(total / count, 2)

def performance_evaluator(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    else:
        return "Needs Improvement"

def expense_checker(budget, cost):
    return budget >= cost


name = input("Enter student name: ")

budget = float(input("Enter monthly budget: "))

total_grades = 0.0
count = 0

while True:
    grade_input = input("Enter a grade or type done: ").lower()
    if grade_input == "done":
        break
    grade = float(grade_input)
    total_grades += grade
    count += 1

average = average_calculator(total_grades, count)
status = performance_evaluator(average)

celebration_cost = float(input("Enter celebration meal cost: "))
affordable = expense_checker(budget, celebration_cost)

print("\nStudent Report")
print("Name:", name)
print("Subjects:", count)
print("Average Grade:", average)
print("Performance:", status)

if affordable:
    print("Celebration meal is affordable.")
else:
    print("Celebration meal is not affordable.")
