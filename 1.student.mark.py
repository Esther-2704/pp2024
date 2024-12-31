# Function to input number of students in a class
def input_number_of_students():
    return int(input("Enter number of students in a class: "))

# Function to input student information
def input_student_info(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student DoB (dd/mm/yyyy): ")
        students.append((student_id, student_name, student_dob))
    return students

# Function to input number of courses
def input_number_of_courses():
    return int(input("Enter number of courses: "))

# Function to input course information
def input_course_info(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

# Function to input marks for students in a selected course
def input_student_marks(students, selected_course):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for student {student[1]} in course {selected_course}: "))
        marks[student[0]] = mark
    return marks

# Function to list courses
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

# Function to list students
def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

# Function to show student marks for a given course
def show_student_marks(marks, course_id, students):
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks.items():
        student_name = next(student[1] for student in students if student[0] == student_id)
        print(f"Student: {student_name}, Mark: {mark}")

# Main function
def main():
    num_students = input_number_of_students()
    students = input_student_info(num_students)
    
    num_courses = input_number_of_courses()
    courses = input_course_info(num_courses)
    
    marks_dict = {}
    
    while True:
        print("\nOptions:\n1. List Courses\n2. List Students\n3. Select a Course and Input Marks\n4. Show Student Marks for a Course\n5. Exit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            list_courses(courses)
        elif choice == 2:
            list_students(students)
        elif choice == 3:
            selected_course = input("Enter course ID to input marks: ")
            marks = input_student_marks(students, selected_course)
            marks_dict[selected_course] = marks
        elif choice == 4:
            course_id = input("Enter course ID to show marks: ")
            if course_id in marks_dict:
                show_student_marks(marks_dict[course_id], course_id, students)
            else:
                print("No marks available for this course.")
        elif choice == 5:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
