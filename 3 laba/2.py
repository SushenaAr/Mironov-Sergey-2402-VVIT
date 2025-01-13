def write_to_file(text, mode):
    with open('user_input.txt', mode, encoding='UTF-8') as file:
        file.write(text)


write_to_file("wа", "w")
write_to_file("wb", "w")

write_to_file("aa", "a")
write_to_file("ab", "a")
