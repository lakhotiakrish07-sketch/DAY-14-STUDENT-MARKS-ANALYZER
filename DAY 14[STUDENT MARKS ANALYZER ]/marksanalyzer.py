# Day 14: Student Marks Analyzer
# Use: list, max(), min(), avg
marks = []
n = int(input("Enter number of students: "))
for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\n--- Marks Analysis ---")
print("Marks List:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
