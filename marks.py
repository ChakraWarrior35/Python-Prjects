def sort_students_by_marks(student_dict):
    students = sorted(student_dict.items(), key=lambda x: x[1], reverse=True)
    return students
student_dict = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    student_dict[name] = marks
sorted_students = sort_students_by_marks(student_dict)
print("Students sorted by marks (descending order):")
for name, marks in sorted_students:
    print(f"{name}: {marks}")