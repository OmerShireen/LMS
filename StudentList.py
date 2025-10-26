from Student import Student
class StudentList:
    def __init__(self):
        self._student_list =[]
        
    @property
    def student_list(self):
        return self._student_list

    def add(self, student: Student):
        self._student_list = self._student_list + [student]

    def add_at(self, index: int, student: Student):
        if index < 0:
            index = 0
        if index > len(self.student_list):
            index = len(self._student_list)
        self._student_list = self._student_list[ :index] + [student] + self._student_list[index:]

    def remove_at(self, index: int):
        if 0 <= index < len(self._student_list):
            self._student_list = self._student_list[:index] + self._student_list[index+1:]

    def search_by_name(self, name: str):
        return[s for s in self._student_list if s.name.lower() == name.lower()]

    def search_by_seat_no(self, seat_no: str):
        return[s for s in self._student_list if s.seat_no == seat_no]

    def __str__(self):
        if not self._student_list:
            return "No students"
        return "\n\n".join(str(s)for s in self._student_list)                                            