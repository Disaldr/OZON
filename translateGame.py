print("Приветствую в игре Словариус! Введите слова и их переводы, а я проведу тестирование по этим словам")
dictionary = {}
while True:
    key = input("Введите слово на английском или stop: ")
    if key == "stop":
        break
    value = input("Введите его перевод или stop: ")
    if value == "stop":
        break
    dictionary[key] = value
