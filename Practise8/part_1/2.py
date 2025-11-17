import json

filenames = ['100kb.json', '200kb.json', '500kb.json']

# открываем одновременно все три JSON-файла и выводим их содержимое на экран
for fname in filenames:
    with open('Practise8/part_1/json/'+fname, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        obj = json.loads(content)  # Преобразование в python-объект