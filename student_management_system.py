class StudentManagementSystem:
    def __init__(self):
        self.student_list = {}
    
    def add_studnet(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student with the given ID already exists.")
            return
        self.students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade
        }
        print("Student added successfully.")

    def view_students(self):
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student with the given ID does not exist.")
    
def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
    
        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            sms.add_student(student_id, name, age, grade)
        
        elif choice == "2":
            sms.view_students()

        elif choice == "3":
            student_id = input("Enter student ID: ")
            sms.remove_student(student_id)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()