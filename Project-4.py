Marks = [36,60,54,95,25,89,54,78,88,75,45,78,45,65,85,90,98,70,50,55]

total_students = len(Marks)

highest_marks = max(Marks)
lowest_marks = min(Marks)
average_marks = sum(Marks) / total_students

passed_count = sum(1 for m in Marks if m >= 40)
failed_count = total_students - passed_count
perfect_scores = Marks.count(100)

pass_percentage = (passed_count / total_students) * 100

print(f"Total Students: {total_students}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Average Marks: {average_marks:.1f}")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}")
print(f"Perfect Scores (100): {perfect_scores}")
print(f"Pass Percentage: {pass_percentage:.1f}%")
print()

ascending_marks = sorted(Marks)
descending_marks = sorted(Marks, reverse=True)

second_lowest = ascending_marks[1] 
second_highest = descending_marks[1]

all_passed = all (m >= 40 for m in Marks)
any_failed = any(m < 40 for m in Marks)

print(f" Ascending Order: {ascending_marks}")
print(f" Descending Order: {descending_marks}")
print(f"Second Lowest Marks: {second_lowest}")
print(f"Second Highest Marks: {second_highest}")
print(f"Did all Students Pass?: {all_passed}")
print(f"Did any Students Fail?: {any_failed}")
print()

grades = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}

for m in Marks:
    if m >= 90:
        grades["A"] += 1
    elif m >= 80:
        grades["B"] += 1
    elif m >= 70:
        grades["C"] += 1
    elif m >= 60:
        grades["D"] += 1
    elif m >= 40:
        grades["E"] += 1
    else:
        grades["F"] += 1

for grade, count in grades.items():
    print(f"{grade}: {count}")