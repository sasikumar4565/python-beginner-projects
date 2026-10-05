print("===== STUDENT MANAGEMENT SYSTEM =====")

students = [
    {
        "name": "Sasi",
        "age": 14,
        "grade": "9"
    },
    {
        "name": "Rahul",
        "age": 14,
        "grade": "9"
    },
    {
        "name": "Anu",
        "age": 13,
        "grade": "8"
    }
]

print("\n===== STUDENT LIST =====")

for student in students:
    print("\nName:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])

print("\nTotal Students:", len(students))

# Search
search_name = "Sasi"

print("\n===== SEARCH RESULT =====")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student Found!")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        found = True

if not found:
    print("Student not found.")
