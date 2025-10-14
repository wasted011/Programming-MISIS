def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_letters = list(set(tokens))
    unique_letters.sort()
    new_dict = {}
    for el in unique_letters:
        new_dict.update({
            el: tokens.count(el)
        })
    return new_dict
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    tuple_list = list(freq.items())
    tuple_list.sort()
    return tuple_list[:n]
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]