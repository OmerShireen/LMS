class Course:
    def __init__(self, course_name, course_num):
        self._course_name = course_name
        self._course_num = course_num

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, new):
        self._course_name = new

    @property
    def course_num(self):
        return self._course_num

    @course_num.setter
    def course_num(self, new):
        self._course_num = new  

    def __str__(self):
        return f"{self._course_name} {self._course_num}"                  