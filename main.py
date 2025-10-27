from Course import Course
from Teacher import Teacher
from Student import Student
from StudentList import StudentList
from CourseList import CourseList
from TeachersList import TeachersList

def main():

    c1 = Course("Object Oriented Programming", "CS201")
    c2 = Course("Discrete Structure", "CS202" )
    c3 = Course("Linear Algebra", "CS203")

    cl = CourseList()
    cl.add(c1)
    cl.add(c2)

    s1 = Student("Omer Shireen", 21, "omer7sce@gmail.com", "03257661921", "b24110006117", 2, cl)
    s2 = Student("Faisal", 20, "faisal@gmail.com", "03297638542", "b24110006042", 2, cl)
    s3 = Student("Shahabuddin", 20, "shahab@gmail.com", "03297538929", "b24110006128", 2, cl)

    t1 = Teacher("Dr. Humera", 40, "humera@ku.edu.pk", "0300000000", "Professor", cl)
    t2 = Teacher("Badar Sami", 55, "badar@ku.edu.pk", "0300000000", "Professor", cl)

    
    students = StudentList()
    teachers = TeachersList()

    students.add(s1)
    students.add(s3)
    teachers.add(t1)
    teachers.add(t2)

   
    print("=== STUDENTS ===")
    print(students)
    print("\n=== TEACHERS ===")
    print(teachers)

    cl.add_at(1, c3)

   
    s2 = Student("Abdullah", 20, "abdullah@mail.com", "0324121765", "b24110006073", 2, cl)
    students.add_at(0, s2)

    print("\nAfter adding course c3 and student s2:")
    print("Courses in cl:")
    print(cl)
    print("\nStudents list:")
    print(students)

if __name__ == "__main__":
    main()
 