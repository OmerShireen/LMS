from Person import Person
from Course import Course
from CourseList import CourseList

class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, phone_no: int, designation: str, assigned_courses= None):
        super().__init__(self, name, age, email, phone_no):
        self._designation = designation

        if assigned_courses = None:
            self._assigned_courses = CourseList()
        elif isinstance(assigned_courses, CourseList):
            self._assigned_courses = assigned_courses
        elif isinstance(assigned_courses, list):
            cl = CourseList()
            for c in assigned_courses:
                cl.add(c)
            self._assigned_courses = cl
        else:
            raise TypeError("assigned courses must be CourseList, List of Course, or None")

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, new):
        self._designation = new

    @property
    def assigned_courses(self):
        return self._assigned_courses

    @assigned_courses.setter
    def assigned_courses(self, new):
        if isinstance(new, CourseList):
            self._assigned_courses = new
        else:
            raise TypeError("assigned_courses must be a CourseList")

    def __str__(self):
        return (
            f"Teacher: {self.name}  | Designation: {self._designation}\n"
            f"Assigned Courses:\n{self._assigned_courses}"
            )        






