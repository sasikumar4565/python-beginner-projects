print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))
social = float(input("Enter Social marks: "))

total = maths + science + english + computer + social
average = total / 5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
