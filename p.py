# Student management details
total_students = 10
students = []

# Function to show all students
def show_students():
    if not students:
        print("No students registered!\n")
    else:
        print("\n--- Student Records ---")

        for s in students:
            print(
                f"Roll Number: {s['roll_no']}, "
                f"Name: {s['name']}, "
                f"Marks: {s['marks']}, "
                f"Percentage: {s['percentage']}%"
            )

        print()

# Function to add a student
def add_student():
    if len(students) >= total_students:
        print("Student limit reached!\n")
        return

    roll_no = input("Enter student roll number: ")

    for s in students:
        if s["roll_no"] == roll_no:
            print("Roll number already exists!\n")
            return

    name = input("Enter student name: ")
    marks = float(input("Enter obtained marks: "))
    total_marks = float(input("Enter total marks: "))

    if total_marks <= 0 or marks < 0 or marks > total_marks:
        print("Invalid marks entered!\n")
        return

    percentage = round((marks / total_marks) * 100, 2)

    students.append({
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total_marks": total_marks,
        "percentage": percentage
    })

    print("Student added successfully!\n")

# Function to search for a student
def search_student():
    roll_no = input("Enter roll number to search: ")

    for s in students:
        if s["roll_no"] == roll_no:
            print("\n--- Student Found ---")
            print(f"Roll Number: {s['roll_no']}")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']} / {s['total_marks']}")
            print(f"Percentage: {s['percentage']}%\n")
            return

    print("Student not found!\n")

# Function to update student details
def update_student():
    roll_no = input("Enter roll number to update: ")

    for s in students:
        if s["roll_no"] == roll_no:
            name = input("Enter new student name: ")
            marks = float(input("Enter new obtained marks: "))
            total_marks = float(input("Enter new total marks: "))

            if total_marks <= 0 or marks < 0 or marks > total_marks:
                print("Invalid marks entered!\n")
                return

            s["name"] = name
            s["marks"] = marks
            s["total_marks"] = total_marks
            s["percentage"] = round((marks / total_marks) * 100, 2)

            print("Student details updated successfully!\n")
            return

    print("Student not found!\n")

# Function to delete a student
def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")

# Main loop
while True:
    print("0. Exit")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting Student Management System...")
        break
    elif choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    else:
        print("Invalid choice, try again.\n")
