
            print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        python_marks = float(input("Enter Python marks: "))
        mathematics_marks = float(input("Enter Mathematics marks: "))
        communication_marks = float(input("Enter Communication marks: "))

        student = Student(
            name,
            age,
            python_marks,
            mathematics_marks,
            communication_marks
        )

        manager.add_student(student)
        print("Student added successfully!")

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        student = manager.find_student(name)

        if student:
            student.display()
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter student name to update: ")

        python_marks = float(input("Enter new Python marks: "))
        mathematics_marks = float(input("Enter new Mathematics marks: "))
        communication_marks = float(input("Enter new Communication marks: "))

        updated = manager.update_student(
            name,
            python_marks,
            mathematics_marks,
            communication_marks
        )

        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        name = input("Enter student name to delete: ")

        deleted = manager.delete_student(name)

        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        save_students(manager.students, "students.json")
        print("Student data saved successfully!")
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")        
