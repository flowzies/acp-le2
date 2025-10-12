class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id = (student_id, student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

    def __str__(self):
        return (f"\nID: {self.id[0]}\nName: {self.id[1]}\nEmail: {self.email}"
                f"\nCourses: {', '.join(self.courses) if self.courses else 'None'}"
                f"\nGrades: {self.grades if self.grades else 'None'}")


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student = Student(student_id, student_name, email, grades, courses)
        self.students.append(student)
        return " Student added successfully."

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return " Student updated successfully."
        return " Student not found."

    def delete_student(self, student_id):
        for student in self.students:
            if student.id[0] == student_id:
                self.students.remove(student)
                return " Student deleted successfully."
        return " Student not found."

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id[0] == student_id:
                student.courses.add(course)
                return "✅ Course enrolled successfully."
        return " Student not found."

    def search_student(self, student_id):
        for student in self.students:
            if student.id[0] == student_id:
                return student
        return " Student not found."


def main():
    records = StudentRecords()

    while True:
        print("\n===== STUDENT RECORDS MANAGEMENT SYSTEM =====")
        print("1. Add a Student")
        print("2. Update a Student")
        print("3. Delete a Student")
        print("4. Enroll in a Course")
        print("5. Search Student by ID")
        print("6. Display All Students")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            email = input("Enter Email: ")

            grades = {}
            add_grades = input("Add grades? (y/n): ").lower()
            if add_grades == "y":
                while True:
                    subject = input("Enter subject name (or 'done' to stop): ")
                    if subject.lower() == "done":
                        break
                    score = float(input(f"Enter score for {subject}: "))
                    grades[subject] = score

            courses = set()
            add_courses = input("Add courses? (y/n): ").lower()
            if add_courses == "y":
                while True:
                    course = input("Enter course name (or 'done' to stop): ")
                    if course.lower() == "done":
                        break
                    courses.add(course)

            print(records.add_student(student_id, student_name, email, grades, courses))

        elif choice == "2":
            student_id = input("Enter Student ID to update: ")
            email = input("Enter new email (leave blank to skip): ")

            grades = {}
            update_grades = input("Update grades? (y/n): ").lower()
            if update_grades == "y":
                while True:
                    subject = input("Enter subject name (or 'done' to stop): ")
                    if subject.lower() == "done":
                        break
                    score = float(input(f"Enter new score for {subject}: "))
                    grades[subject] = score

            courses = set()
            update_courses = input("Update courses? (y/n): ").lower()
            if update_courses == "y":
                while True:
                    course = input("Enter new course (or 'done' to stop): ")
                    if course.lower() == "done":
                        break
                    courses.add(course)

            print(records.update_student(student_id, email, grades, courses))

        elif choice == "3":
            student_id = input("Enter Student ID to delete: ")
            print(records.delete_student(student_id))

        elif choice == "4":
            student_id = input("Enter Student ID to enroll in a course: ")
            course = input("Enter course name: ")
            print(records.enroll_course(student_id, course))

        elif choice == "5":
            student_id = input("Enter Student ID to search: ")
            student = records.search_student(student_id)
            print(student)

        elif choice == "6":
            print("\nAll Students:")
            if not records.students:
                print("No students available.")
            else:
                for s in records.students:
                    print(s)

        elif choice == "7":
            print(" Exiting program. Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
