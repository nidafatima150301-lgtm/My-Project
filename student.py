class Students:

    def __init__(self):
        self.student = {}

    # Add Student
    def add(self):
        roll = int(input("Enter Roll No: "))

        if roll in self.student:
            print("Roll Number Already Exists")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        self.student[roll] = {
            "name": name,
            "age": age,
            "course": course
        }

        print("Student Added Successfully")

    
    def search(self):

        roll = int(input("Enter Roll No to Search: "))

        if roll in self.student:

            print("Student Found")
            print("Roll No :", roll)
            print("Name    :", self.student[roll]["name"])
            print("Age     :", self.student[roll]["age"])
            print("Course  :", self.student[roll]["course"])

        else:
            print("Student Not Found")

    
    def delete(self):

        roll = int(input("Enter Roll No to Delete: "))

        if roll in self.student:

            del self.student[roll]
            print("Student Deleted Successfully")

        else:
            print("Student Not Found")


obj = Students()

while True:

    print("""
========= STUDENT MANAGEMENT =========

1. Add Student
2. Search Student
3. Delete Student
4. Exit

=====================================
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        obj.add()

    
    elif choice == "2":
        obj.search()


    elif choice == "3":
        obj.delete()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")