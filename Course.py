class Course:
    def __init__(self, courseName, courseNum):
        self._courseName = courseName
        self._courseNum = courseNum

    @property
    def courseName(self):
        return self._course_name

    @courseName.setter
    def course_name(self, new):
        self._courseName = new

    @property
    def courseNum(self):
        return self._courseNum

    @courseNum.setter
    def course_num(self, new):
        self._courseNum = new  

    def __str__(self):
        return f"{self._courseName} {self._courseNum}"                  