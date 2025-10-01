notes = tuple([input().strip(), input().strip(), float(input())])
print(notes)
def format_record(notes):
    initials = ''
    fio, group, gpa = notes[0].strip().split() , notes[1].strip(), notes[2]
    if len(fio) < 2 or len(fio) > 3:
        return TypeError
    if len(group) == 0:
        return ValueError
    for el in range(len(fio)):
        if fio[el][0].isupper() == False:
            fio[el] = fio[el].capitalize()
    for el3 in range(1, len(fio)):
        initials += fio[el3][0] + "."
    return f"{fio[0]} {initials}, гр. {group}, GPA {gpa:.2f}"
print(format_record(notes))