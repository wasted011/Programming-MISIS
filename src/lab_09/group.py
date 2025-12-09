import sys
from pathlib import *

sys.path.append('src')
from _functions_ import *

class group:

    def __init__(self, csv_file: str | Path = "data/lab_09/group.csv", json_file: str | Path = "data/lab_09/group.json", student_list: list = []):
        self.csv_file = csv_file
        self.json_file = json_file
        self.student_list = student_list
   
    def students_list(self):
        if is_not_empty(self.csv_file):
            print("------------")
            for element in self.student_list:
                print(f"Фио: {element["fio"]}, Группа: {element["group"]}, Дата рождения: {element["birthdate"]}, GPA: {element["gpa"]}")
            return "------------"
        elif not is_not_empty(self.csv_file):
            return "Файл пуст"
    
    def add_student(self, fio: str, birthdate: str, group: str, gpa: float):
        new_student = {"fio": fio, "birthdate": birthdate, "group": group, "gpa": gpa}
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] != fio:
                    self.student_list.append(new_student)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                    return "Успешное добавление"
            return "Студент уже существует"
        self.student_list.append(new_student)
        write_json(self.student_list, self.json_file)
        json_to_csv(self.json_file, self.csv_file)
        return "Успешное добавление"
    
    def find_student(self, fio: str):
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    return f"Фио: {element["fio"]}, Дата рождения: {element["birthdate"]}, Группа: {element["group"]}, GPA: {element["gpa"]}"
            return "Фио не найдено"
        else:
            return "Список пуст"
    
    def remove_student(self, fio: str):
        if len(self.student_list) != 0:
            for element in self.student_list:
                if element["fio"] == fio:
                    self.student_list.remove(element)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                    return "Успешное удаление"
            return "Фио не найдено"
        return "Список пуст"
        
    def update_student(self, fio: str):
        updated_student = {"fio": fio, "birthdate": input(": "), "group": input(": "), "gpa": input(": ")}
        if len(self.student_list) != 0:
            for index in range(len(self.student_list)):
                if self.student_list[index]["fio"] == fio:
                    self.student_list.remove(self.student_list[index])
                    self.student_list.insert(index, updated_student)
                    write_json(self.student_list, self.json_file)
                    json_to_csv(self.json_file, self.csv_file)
                    return "Успешное обновление"
            return "Фио не найдено"
        return "Список пуст"
    
    def read_all(self):
        if is_not_empty(self.csv_file):
            return read_text(self.csv_file)
        return "Файл пуст"

assert group().add_student("smth", "smth", "smth", 4.6) == "Успешное добавление"
assert group().add_student("maria", "10/10/2000", "bivt", 4.3) == "Успешное добавление"
assert group().update_student("maria") == "Успешное обновление"
assert group().remove_student("maria") == "Успешное удаление"
