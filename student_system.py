import os

FILE_NAME = "students.txt"

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = input("Marks: ")
    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("Student added successfully!")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            print(line.strip())

# Menu Loop
while True:
    print("\n1. Add | 2. View | 3. Exit")
    choice = input("Select option: ")
    if choice == '1': add_student()
    elif choice == '2': view_students()
    elif choice == '3': break
    else: print("Invalid Input!")