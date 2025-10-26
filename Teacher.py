from teacher import Teacher

class TeachersList:
    def __init__(self):
        self._teachers_list = []   

    @property
    def teachers_list(self):
        return self._teachers_list

    def add(self, teacher: Teacher):
        self._teachers_list = self._teachers_list + [teacher]

    def add_at(self, index: int, teacher: Teacher):
        if index < 0:
            index = 0
        if index > len(self._teachers_list):
            index = len(self._teachers_list)
        self._teachers_list = self._teachers_list[:index] + [teacher] + self._teachers_list[index:]

    def remove(self, teacher: Teacher):
        self._teachers_list = [t for t in self._teachers_list if t is not teacher]

    def remove_at(self, index: int):
        if 0 <= index < len(self._teachers_list):
            self._teachers_list = self._teachers_list[:index] + self._teachers_list[index+1:]

    def search_by_name(self, name: str):
        return [t for t in self._teachers_list if t.name.lower() == name.lower()]

    def search_by_designation(self, designation: str):
        return [t for t in self._teachers_list if t.designation.lower() == designation.lower()]

    def __str__(self):
        if not self._teachers_list:
            return "No teachers"
        return "\n\n".join(str(t) for t in self._teachers_list)
