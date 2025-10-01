list_01 = list(map(int, input().split()))
def min_max(list_def):
    if len(list_def) == 0:
        return ValueError
    return min(list_def), max(list_def) 
print(min_max(list_01))