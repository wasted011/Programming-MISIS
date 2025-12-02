import json, sys
sys.path.append("src")

from _functions_ import *
from dataclasses import *
from datetime import *
# imports

# imports

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    student_list = []

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Неверный формат даты")
        
        if not (0 <= self.gpa <= 10):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        birth_year = int(self.birthdate.split("/")[0])
        today_year = int(date.today().year)
        return today_year - birth_year

    def to_dict(self) -> dict:
        new_student = {"fio": self.fio, "birthdate": self.birthdate, "group": self.group, "gpa": self.gpa}
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] != self.fio:
                    self.student_list.append(new_student)
                    return "Успешное добавление"
                else:
                    return "Студент существует"
        else:
            self.student_list.append(new_student)
            return "Успешное добавление"
    def from_dict(self, fio: str):
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    return element
                else:
                    return "Фио не найдено"
        else:
            return "Пустой список"

    def __str__(self):
        return f"Фио: {self.fio}, Дата рождения: {self.birthdate}, Группа: {self.group}, GPA {self.gpa}"
    
assert Student("dmitriy", "2000/12/01", "bivt", 4.6).age() == 25
assert Student("dmitriy", "2000/12/01", "bivt", 4.6).to_dict() == "Успешное добавление"
assert Student("dmitriy", "2000/12/01", "bivt", 4.6).from_dict("dmitriy") == {'fio': 'dmitriy', 'birthdate': '2000/12/01', 'group': 'bivt', 'gpa': 4.6}
assert Student("dmitriy", "2000/12/01", "bivt", 4.6).__str__() == "Фио: dmitriy, Дата рождения: 2000/12/01, Группа: bivt, GPA 4.6"