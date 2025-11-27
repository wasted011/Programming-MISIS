# imports
import json, sys
sys.path.append("src")

from _functions_ import *

def write_json(item: dict, json_path: str | Path):
    with Path(json_path).open('w', newline = '', encoding = 'utf-8-sig') as file:
        json.dump(item, file, indent = 2, ensure_ascii = False)

class student:

    def __init__(self, json_file: str | Path, students_dict: list = []):
        self.json_file = json_file
        self.students_list = students_dict

    def to_dict(self, fio: str, birthdate: str, group: str, gpa: float):
        new_student = {"fio": fio, "birthdate": birthdate, "group": group, "gpa": gpa}
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] != 0:
                    self.students_list.append(new_student)
                    write_json(self.students_list, self.json_file)
                    return "Успешно" 
        self.students_list.append(new_student)
        write_json(self.students_list, self.json_file)
        return "Успешно"
    
    def from_dict(self, fio: str):
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] == fio:
                    self.students_list.remove(element)
                    write_json(self.students_list, self.json_file)
                    return "Успешное удаление"
            return "Фио не найдено"
        return "Список пуст"
    
    def get_info(self, fio: str):
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] == fio:
                    return f"Фио: {element["fio"]}, Дата рождения: {element["birthdate"]}, Группа: {element["group"]}, GPA: {element["gpa"]}"
            return "Фио не найдено"
        return "Список пуст"

assert student("data/lab_08/students.json").to_dict("EEE", "10.08.2000", "BIVT-24", 4.65) == "Успешно"
assert student("data/lab_08/students.json").to_dict("AAA", "30.10.2004", "BIVT-23", 3.5) == "Успешно"
assert student("data/lab_08/students.json").from_dict("AAA") == "Успешное удаление"
assert student("data/lab_08/students.json").get_info("EEE") == "Фио: EEE, Дата рождения: 10.08.2000, Группа: BIVT-24, GPA: 4.65"
