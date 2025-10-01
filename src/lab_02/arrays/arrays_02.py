list_02 = list(map(int, input().split()))
def unique_sorted(list_def):
    return sorted(set(list_def))
print(unique_sorted(list_02))