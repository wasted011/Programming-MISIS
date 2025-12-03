import sys
from pathlib import *

sys.path.append('src')
from _functions_ import *

class Group:
    
    def __init__(self, csv_file: str | Path = "data/lab_09/group.csv", students_list = []):
        self.csv_file = csv_file
        self.students_list = students_list

    def list(self):
        if len(self.students_list) != 0:
            for element in self.students_list:
                print(f"Фио: {element["fio"]}, Дата рождения: {element["birthdate"]}, Группа: {element["group"]}, GPA: {element["gpa"]}")
        else:
            return "Список пуст"
    
    def add_student(self, fio: str, birthdate: str, group: str, gpa: float):
        new_student = {"fio": fio, "birthdate": birthdate, "group": group, "gpa": gpa}
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] != fio:
                    self.students_list.append(new_student)
                    write_csv_lib([values for keys, values in element.items()], self.csv_file, [keys for keys, values in element.items])
                    return "Успешное добавление"
                else:
                    return "Студент уже существует"
        else:
            self.students_list.append(new_student)
            for element in self.students_list:
                write_csv_lib([values for keys, values in element.items()], self.csv_file, [keys for keys, values in element.items()])
                return "Успешное добавление"

    def find_student(self, fio: str):
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] == fio:
                    return f"Фио: {element["fio"]}, Дата рождения: {element["birthdate"]}, Группа: {element["group"]}, GPA: {element["gpa"]}"
                else:
                    return "Студент не найден"
        else:
            return "Список пуст"
    
    def remove_student(self, fio: str):
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] == fio:
                    self.students_list.remove(element)
                    write_csv_lib([values for keys, values in element.items()], self.csv_file)
                    return "Успешное удаление"
                else:
                    return "Студент не найден"
        else:
            return "Список пуст"
    
    def update_student(self, fio: str):
        updated_info = {"fio": fio, "birthdate": input("Введите дату рождения: "), "group": input("Введите наименование группы: "), "gpa": input("Введите GPA: ")}
        if len(self.students_list) != 0:
            for element in self.students_list:
                if element["fio"] == fio:
                    self.students_list.remove(element)
                    self.students_list.append(updated_info)
                    write_csv_lib([values for keys, values in element.items()], self.csv_file, header = None)
                    return "Информация обновлена"
                else:
                    return "Студент не найден"
        else:
            return "Список пуст"
    
    def _read_all(self):
        return read_text(self.csv_file)

assert Group().add_student("evgeny", "2000", "bivt", 4.6) == "Успешное добавление"