def format_record(rec: tuple[str, str, float]) -> str:
    initials = ''
    fio, group, gpa = rec[0].strip().split(), rec[1], rec[2]
    if len(fio) > 3 or len(fio) < 2:
        return ValueError
    if not isinstance(gpa, float):
        return TypeError
    for index_01 in range(len(fio)):
        fio[index_01] = fio[index_01].capitalize()
        for el in fio[index_01]:
            if el.isupper():
                initials += el + "."
    return f"{fio[0]} {initials[2:]}, гр. {group}, GPA {gpa:.2f}"
print(format_record(("     сидорова   анна   сергеевна    ", "BIVT-25", 4.6)))