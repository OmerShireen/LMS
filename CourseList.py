from Course import Course

class CourseList:
    def __init__(self):
        self._course_list =[]

    def add(self, course: Course):
        self._course_list = self._course_list + [course]    

    def add_at(self, index: int, course: Course):
        if index < 0:
            index = 0
        if index > len(self._course_list):
            index = len(self._course_list)
        self._course_list = self._course_list[:index] + [course] + self._course_list[index:]

    def remove(self, course: Course):
        self._course_list = [c for c in self._course_list if c is not course]

    def remove_at(self, index: int):
        if 0 <= index < len(self._course_list):
            self._course_list = self._course_list[:index] + self._course_list[index+1:]

    def search_by_courseName(self, courseName: str):
        return [c for c in self._course_list if c.courseName.lower() == courseName.lower()]    

    def search_by_courseNum(self, courseNum: str):
        return [c for c in self._course_list if c.courseNum == courseNum]

    def __str__(self):
        if not self._course_list:
            return "No courses"
        return "\n".join(str(c) for c in self._course_list)                                 