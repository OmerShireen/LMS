from Person import Person
from Course import Course
from CourseList import CourseList

class Student(Person):
    def __init__(self, name: str, age: int, email: str, phone_no: int, rollNo: str, semester:int, courses=None):
        super().__init__(name, age, email, phone_no)
        self._rollNo = rollNo
        self._semester = semester

    if courses is None:
        self._courses = CourseList()
    elif isinstance(courses, CourseList):
        self._courses = courses
    elif isinstance(courses, list):
        cl = CourseList()
        for c in course:
            c1.add(c)
        self._courses = cl
    else:
        raise TypeError("courses must be CourseList, list of Course, or None")

    @property
    def rollNo(self):
        return self._rollNo

    @rollNo.setter
    def rollNo(self, new):
        self._rollNo = new

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, new):
        self._semester = new

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, new):
        if isinstance(new, CourseList):
            self._courses = new
        else:
            raise TypeError("courses must be CourseList")

    def __str__(self):
        return f" {self._name} | Seat No: {self._seatNo} | Semester: {self._semester}\n"
        f"Courses:\n{self._courses}"                   
