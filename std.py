

print("================================")
print("   STUDENT GRADE MANAGEMENT")
print("================================")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

print("\nEnter Marks (out of 100)")

python = float(input("Python: "))
ai = float(input("Artificial Intelligence: "))
ml = float(input("Machine Learning: "))
excel = float(input("Excel: "))
data_analysis = float(input("Data Analysis: "))

marks = [python, ai, ml, excel, data_analysis]

total = sum(marks)
average = total / len(marks)

# Calculate grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if all(mark >= 35 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"

print("\n================================")
print("       STUDENT REPORT")
print("================================")

print("Student Name:", name)
print("Roll Number:", roll_no)
print("Python Marks:", python)
print("AI Marks:", ai)
print("ML Marks:", ml)
print("Excel Marks:", excel)
print("Data Analysis Marks:", data_analysis)

print("--------------------------------")
print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2), "%")
print("Grade:", grade)
print("Result:", result)
print("================================")
