documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }

def people(documents):
    doc_number = input("Введите номер документа: ")
    for x in documents:
        if x['number'] == doc_number:
            return x['name']
    return "Пользователь не найден"

def shelf(directories):
    document_number = input("Введите номер документа: ")
    for i in directories:
        if document_number in directories[i]:
            return i
    return "Документ не найден"

def lst(documents):
    for i in documents:
        print(i['type'], i['number'], i['name'])
    print()

def add():
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите номер документа: ")
    doc_owner = input("Введите имя владельца документа: ")
    shelf_id = input("Введите номер полки {} : ".format(directories.keys()))
    if shelf_id not in directories:
        return "Полки не существует"
    new_doc = dict(type=doc_type, number=doc_number, name=doc_owner)
    documents.append(new_doc)
    directories[shelf_id] += [doc_number]
    return "Документ успешно добавлен"

def add_shelf():
    number = input("Введите номер новой полки: ")
    directories.setdefault(number, [])
    return 'Изменения внесены'

def delete():
    doc_number = input("Введите номер документа, который хотите удалить: ")
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d["number"] == doc_number:
            documents.pop(i)
    if initial_len == len(documents):
        return "Документа не существует"
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
    return "Документ успешно удален"

def move():
    doc_number = input("Введите номер документа, который хотите переместить: ")
    shelf_id = input("Введите номер полки, на которую хотите переместить документ: ")
    doc_existence = False
    if shelf_id not in directories:
        return "Полки не существует"
    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf_id] += [doc_number]
            value.remove(doc_number)
    if doc_existence:
        return "Документ успешно перемещен"
    else :
        return "Документ не существует"

def call():
    while True:
        call_func = input("Введите название функции чтобы её вызвать: ")
        for i in call_func:
            if call_func == 'p':
                print (people(documents))
                break
            elif call_func == 's':
                print (shelf(directories))
                break
            elif call_func == 'l':
                print (lst(documents))
                break
            elif call_func == 'a':
                print (add())
                break
            elif call_func == 'a_s':
                print (add_shelf())
                break
            elif call_func == 'd':
                print (delete())
                break
            elif call_func == 'm':
                print (move())
                break
            elif call_func == 'q':
                print ('Goodbye')
                break
            else:
                print('Введена неверная функция!')
call()