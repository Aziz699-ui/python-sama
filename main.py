def naz(replace):
    with open("file.bin", "rb") as file:
        binary = file.read()

    text = binary.decode('utf-8')
    for old, new in replace.items():
        text = text.replace(old, new)

    new_binary = text.encode('utf-8')

    with open("file.bin", "wb") as file:
        file.write(new_binary)

num1 = input("Введите старое слово:")
num2 = input("Введите новое слово:")
replacements = {num1: num2}
naz(replacements)
