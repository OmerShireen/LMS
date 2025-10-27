from Person import Person
from Course import Course
from CourseList import CourseList

class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, phone_no: int, designation: str, assigned_courses= None):
        super().__init__(name, age, email, phone_no)
        self._designation = designation

        if assigned_courses is None:
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
    def teachers_list(self):
        return self._teachers_list

    def add(self, teacher):
        self._teachers_list = self._teachers_list + [teacher]

    def add_at(self, index: int, teacher):
        if index < 0:
            index = 0
        if index > len(self._teachers_list):
            index = len(self._teachers_list)
        self._teachers_list = self._teachers_list[:index] + [teacher] + self._teachers_list[index:]

    def remove(self, teacher):
        self._teachers_list = [t for t in self._teachers_list if t is not teacher]

    def remove_at(self, index: int):
        if 0 <= index < len(self._teachers_list):
            self._teachers_list = self._teachers_list[:index] + self._teachers_list[index+1:]

    def search_by_name(self, name: str):
        return [t for t in self._teachers_list if t.name.lower() == name.lower()]

    def search_by_designation(self, designation: str):
        return [t for t in self._teachers_list if t.designation.lower() == designation.lower()]

    def __str__(self):
        return (
            f"Teacher: {self.name}  | Designation: {self._designation}\n"
            f"Assigned Courses:\n{self._assigned_courses}"
            )        






