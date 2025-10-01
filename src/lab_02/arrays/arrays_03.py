list_03 = [[1,2], (3,4), [5,6], (7,8)]
def flatten(list_def):
    empty = []
    for el in list_def:
        if isinstance(el, (list, tuple)) == False:
            return TypeError
        else:
            empty += el
    return empty
print(flatten(list_03))
            