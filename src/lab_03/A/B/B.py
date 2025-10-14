import re
def script(text: str, n: int = 5):
    print("---------")
    text = text.casefold().replace("Ё", "Е").replace("ё", "е")
    text = re.sub(r"[\t\r\n]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.findall(r"\w+(?:-\w+)*", text)
    len_unique_words = len(list(set(text)))
    total_words = len(text)
    unique_words = list(set(text))
    unique_words.sort()
    print(f"Всего слов: {total_words}")
    print(f"Уникальных: {len_unique_words}")
    print(f"Топ-5: {len(unique_words[:n])}")
    for el in unique_words[:n]:
        print(f"{el}: {text.count(el)}")
    return "---------"
print(script(""))