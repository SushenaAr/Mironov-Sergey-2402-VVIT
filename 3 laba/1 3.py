def read_file(is_line):
    try:
        with open('example.txt', 'r', encoding='UTF-8') as file:
            if !is_line:
                content = file.read()
                print(content)
            else:
                for line in file:
                    print(line, end='')
    except FileNotFoundError:
        print("Файл example.txt не найден")


read_file(is_line_reading=False)
print()
read_file(is_line_reading=True)
