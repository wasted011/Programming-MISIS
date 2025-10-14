import re
def tokenize(text: str) -> list[str]:
    text = text.casefold().replace("Ё", "Е").replace("ё", "е")
    text = re.sub(r"\t\r\n", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return re.findall(r"\w+(?:-\w+)*", text)
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]