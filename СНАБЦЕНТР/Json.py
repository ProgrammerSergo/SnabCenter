import json

# Функция вывода сообщения
def Print(prints) -> str:
    prints = "Json-файл успешно записан!"
    print(prints)

# Функция извлечения данных из Json и формирует в нужный формат
def proc_json(json_data):
    items = json_data['items']
    source = json_data['source']
    item_id = [item['id'] for item in items]

    # result - словарь для присваивания нужных компонентов
    result = {
        'items' : item_id,
        'source - id' : source,
        'item - id' : item_id[0]
    }
# Возвращаем словарь
    return result

with open("IN.json") as f:
    data_js = json.loads(f.read()) # парсим JSON для извлечения и обработки данных, закодированных в формате JSON.

res = proc_json(data_js) #Обработка данных с помощью функции

# Для создания и считывания файла
with open("OUT.json", "w", encoding = 'utf-8') as f:
    f.write(json.dumps(res, indent=4, ensure_ascii = False))
    Print(prints="Json-файл успешно записан!")

# для открытия и считывания файла
with open("OUT.json", "r", encoding = 'utf-8') as f:
    IN = json.loads(f.read())
    print(IN) 

    # "IN" - входные данные Json
    # "OUT" - выходные данные Json
    # "lenght" - длина хлыста
    # "count" - кол-во
    # "Id" - идентификатор
