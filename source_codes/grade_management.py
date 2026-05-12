student_grade = { }

def add_student(name,grade):
    student_grade[name] = grade
    print(f"{name} is added in system with {grade} marks")

def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}  with marks {grade} is Updated")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} is Deleted")
    else:
        print(f"{name} is not found!")
    
def display_all():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print(f"students not found!")

def main():
    while True:
        print("\n---- Student grade management system ----")
        print("1. add student\n2. update student\n3. delete student\n4. view student\n5. exit\n")
        choice=int(input("Enter your choice :"))
        if choice==1:
            name= input("enter student name :")
            grade=int(input("Enter student grade :"))
            add_student(name,grade)
        elif choice==2:
            name= input("enter student name :")
            grade=int(input("Enter student grade :"))
            update_student(name,grade)
        elif choice==3:
            name= input("enter student name :")
            delete_student(name)
        elif choice==4:
            display_all()
        elif choice==5:
            print("\nSigning off...\nSee you again :)\n")   
            break
        else:
            print("Invalid")

main()