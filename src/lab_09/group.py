import sys
from pathlib import *

sys.path.append('src')
from _functions_ import *

class group:
    def __init__(self, csv_file: str | Path, json_file: str | Path, student_list: list = []):
        self.csv_file = csv_file
        self.json_file = json_file
        self.student_list = student_list
    def student_list(self):
        return read_text(self.csv_file)
    def add_student(self, fio: str, birthdate: str, group: str, gpa: float):
        new_student = {"fio": fio, "birthdate": birthdate, "group": group, "gpa": gpa}
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] != fio:
                    self.student_list.append(new_student)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                return "Успешно"
        self.student_list.append(new_student)
        write_json(self.student_list, self.json_file)
        json_to_csv(self.json_file, self.csv_file)
        return "Успешно"
    def find_student(self, fio: str):
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    return f"Фио: {element["fio"]}, Дата рождения: {element["birthdate"]}, Группа: {element["group"]}, GPA: {element["gpa"]}"
            return "Фио не существует"
        return "Список пуст"
    def remove_student(self, fio: str):
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    self.student_list.remove(element)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                    return "Успешное удаление"
            return "Фио не существует"
    def update_info(self, fio: str):
        new_info = {"fio": fio, "birthdate": input(": "), "group": input(": "), "gpa": float(input(": "))}
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    self.remove_student(fio)
                    self.student_list.append(new_info)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                    return "Успешно обновление информации"
            return "Фио не существует"
        return "Список пуст"

assert group('data/lab_09/group.csv', 'data/lab_09/group.json').add_student("dmitriy", "28.09", "bivt", 4.6) == "Успешно"
assert group('data/lab_09/group.csv', 'data/lab_09/group.json').add_student("dmitrsssssiy", "28.09", "bivt", 4.6) == "Успешно"
assert group('data/lab_09/group.csv', 'data/lab_09/group.json').remove_student("dmitrsssssiy") == "Успешное удаление"
assert group('data/lab_09/group.csv', 'data/lab_09/group.json').find_student("dmitriy") == "Фио: dmitriy, Дата рождения: 28.09, Группа: bivt, GPA: 4.6"