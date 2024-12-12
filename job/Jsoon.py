import json
import math 

# Функция вывода сообщения
def Print() -> str:
    prints = "Json-файл успешно записан!"
    print(prints)

# Функция извлечения данных из Json и формирует в нужный формат
def proc_json(json_data):
    items = json_data['items']
    source = input("Введите значение source: ")
    item_id = input("Введите ID:")

# result - это списки для записи json-файла
    result = {
        'items' : item_id,
        'source - id' : source,
        'item - id' : item_id[0]
    }
    # Реализовано условие для нахождения общего числа(Count) и (Source) --> Доделаю
    if source and items and item_id == 'Ответ(Count)':
        with open("OUT.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(res, indent=4, ensure_ascii = False))
    try:
        Print(prints="Json-файл успешно записан!")
    except TypeError:
        print(f"Ошибка в программном коде: {TypeError}")
# Возвращаем список
    return result

# парсим JSON для извлечения и обработки данных, закодированных в формате JSON
with open("IN.json") as f:
    data_js = json.loads(f.read())

#Обработка данных с помощью функции
res = proc_json(data_js)    

# Для создания и считывания файла
with open("OUT.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(res, indent=4, ensure_ascii = False))
    try:
        Print(prints="Json-файл успешно записан!")
    except TypeError:
        print(f"Ошибка в программном коде: {TypeError}")
with open("OUT.json", "r", encoding = 'utf-8') as f:
    IN = json.loads(f.read())
    print(IN)    

    # "IN" - входные данные Json
    # "OUT" - выходные данные Json
    # "lenght" - длина хлыста
    # "count" - кол-во
    # "Id" - идентификатор
