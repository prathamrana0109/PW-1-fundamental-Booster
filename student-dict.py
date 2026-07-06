students = [
    {
    "id": 101, 
    "name": "Pratham",
    "age": 17,
    "subject": "python", 
    "marks": 90, 
    "grade": "A++",
     "birthday": "2008-09-01"
     },

    {"id": 102, 
    "name": "Eliskaa", 
    "age": 18,
    "subject": "python", 
    "marks": 85,
    "grade": "A+",
     "birthday": "2008-11-12"
     }, 
    
    {"id": 103, 
    "name": "Kwini", 
    "age": 19,
    "subject": "python", 
    "marks": 95,
    "grade": "A++",
     "birthday": "2007-12-24"
     },

    {
    "id": 104, 
    "name": "Khyati", 
    "age": 18,
    "subject": "python", 
    "marks": 81,
    "grade": "A+",
     "birthday": "2008-08-01"
     },

    {"id": 105, 
    "name": "Urvashi", 
    "age": 19,
    "subject": "python", 
    "marks": 80,
    "grade": "B",
     "birthday": "2003-05-01"
     },

    {"id": 106, 
    "name": "Akshara", 
    "age": 17,
    "subject": "python", 
    "marks": 85,
    "grade": "B+",
     "birthday": "2000-02-01"
    },

    {"id": 107, 
    "name": "Ankit", 
    "age": 19,
    "subject": "python", 
    "marks": 90,
    "grade": "A",
     "birthday": "2003-05-01"
     },
]
print("===============Welcome to Student Management System===============")
while True: 
    print("1. Add student ")
    print("2. View student ")
    print("3. Update student ")
    print("4. Delete  student's ")
    print("5. Display Subjects offered")
    print("6. Exit")  
    choice = int(input("Enter your choice : "))
    if choice == 1:
        id = int(input("Enter student id : "))
        name = input("Enter student name : ")
        subject = input("Enter student subject : ")
        marks = int(input("Enter student marks : "))
        grade = input("Enter student grade : ")
        birthday = input("Enter student birthday : ")
        age = int(input("Enter student age : "))
        students.append({"id": id, "name": name, "subject": subject, "marks": marks, "grade": grade, "birthday": birthday, "age": age})
        print("Student record added successfully!")

    elif choice == 2:
        print("Student Records:")
        for s in students:
            print("---------------------------------------------------------------------------------------")
            print(f"ID: {s['id']}, Name: {s['name']}, Subject: {s['subject']}, Marks: {s['marks']}, Grade: {s['grade']}, Birthday: {s['birthday']}, Age: {s['age']}")

    elif choice == 3:
        id = int(input("Enter student id to update : "))
        for s in students:
            if s['id'] == id:
                name = input("Enter new student name : ")
                subject = input("Enter new student subject : ")
                marks = int(input("Enter new student marks : "))
                grade = input("Enter new student grade : ")
                birthday = input("Enter new student birthday : ")
                age = int(input("Enter new student age : "))
                s['name'] = name
                s['subject'] = subject
                s['marks'] = marks
                s['grade'] = grade
                s['birthday'] = birthday
                s['age'] = age
                print("Student record updated successfully!")
                break

    elif choice == 4:
        delete_id = int(input("Enter student id to delete : "))
        for s in students:
            if s['id'] == delete_id:
                students.remove(s)
                print("Student record deleted successfully!")
                break

    elif choice == 5:
        print("Subjects offered:")
        print(" 1. Python")
        print(" 2. Photo Shop")
        print(" 3. Coding")
        print(" 4. AI/ML")
        print(" 5. Data Science")
        print(" 6. Promt engineer")
        print(" 7. Premier pro ")
        print(" 8. Java ")
        print(" 9. C++ ")
        print(" 10. Graphics ")
        

    elif choice == 6:
        print("Thank you for using the Student Management System....!")
        break
    else:
        print("Invalid choice.......!")