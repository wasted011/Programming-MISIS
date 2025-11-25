def format_record(rec: tuple[str, str, float]) -> str:
    initials = ""
    if not isinstance(rec, tuple):
        return TypeError
    if (
        not isinstance(rec[0], str)
        or not isinstance(rec[1], str)
        or not isinstance(rec[2], float)
    ):
        return TypeError
    if len(rec[0].strip().split()) < 2 or len(rec[0].strip().split()) > 3:
        return ValueError
    if len(rec[1]) == 0:
        return TypeError
    fio, group, gpa = rec[0].strip().split(), rec[1].strip(), rec[2]
    for index_01 in range(len(fio)):
        fio[index_01] = fio[index_01].capitalize()
        for el in fio[index_01]:
            if el.isupper():
                initials += el + "."
    return f"{fio[0]} {initials[2:]}, гр. {group}, GPA: {gpa:.2f}"


print(format_record(("    петров    пётр      павлович     ", "IKBO-12", 3.999)))
