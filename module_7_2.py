def custom_write(file_name, strings):
    dict_position_in_file = {}
    line_number = 1
    name = open(file_name, 'w', encoding='utf-8')
    for line in strings:
        dict_position_in_file[(line_number, name.tell())] = line
        name.write(f'{line}\n')
        line_number += 1

    return dict_position_in_file


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
