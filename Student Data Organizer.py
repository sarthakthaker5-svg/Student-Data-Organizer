students_list = []
subjects_set = set()

print("Welcome to Student Data Organizer!")
while True:
    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Sbjects Offered")
    print("6. Exit")
    
    choice = input("Enter your choice:")
    if choice =='1':
        sid=input("Student ID:")
        name=input("Name:")
        age=int(input("Age:"))
        grade=input("Grade:")
        dob=input("Date of Birth (YYYY-MM-DD):")
        subjects=input("Subjects (comma separated):").split(',')
        
        #subjects = [s.strip() for s in subjects]
        student_tuple = (sid, dob)
        
        student = {"info": student_tuple,"name": name,"age": age,"grade": grade,"subjects": subjects}
        students_list.append(student)
        
        for sub in subjects:
            subjects_set.add(sub)
            print("Student added successfully!")
            
    elif choice == '2':
        print("\n Student Records")
        for s in students_list:
            print(f"ID: {s['info'][0]} | "f"Name: {s['name']} | "f"Age: {s['age']} | "f"Grade: {s['grade']} | "f"Subjects: {', '.join(s['subjects'])}")
            
    elif choice == '3':
        sid = input("Enter Student ID to update:")
        for s in students_list:
            if s['info'][0] == sid:
                s["age"]=int(input("New Age:"))
                s["subjects"]=input("New Subjects (comma separated):").split(',')
                
                #s["subjects"] = [x.strip() for x in s["subjects"]]
                
                for sub in s["subjects"]:
                    subjects_set.add(sub)
                    
                    print("Student updated successfully!")
                    
    elif choice == '4':
        sid = input("Enter Student ID to delete: ")
        for i in range(len(students_list)):
            if students_list[i]["info"][0] == sid:
                del students_list[i]
                print("Student deleted successfully!")
                
    elif choice == '5':
        print("\nSubjects Offered:")
        for sub in subjects_set:
            print(sub)
            
    elif choice == '6':
        print("Thank You for using Student Data Organizer. Goodbye!")
        break
    
    else:
        print("Invalid Choice")
        
        
                
            
        
        