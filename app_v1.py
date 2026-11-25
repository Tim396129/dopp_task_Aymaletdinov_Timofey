kn = 0

print("=== Учёт книг ===")

while True:
    print()
    print("Меню:")
    print("1 - Выдать книгу")
    print("2 - Показать, сколько книг выдано")
    print("3 - Сбросить счётчик")
    print("0 - Выход")

    k = input("Введите команду: ")

    if k == "1":
        kn = kn + 1
        print("Книга выдана. Выдано всего:", kn)
    elif k == "2":
        print("Книг выдано:", kn)
    elif k == "3":
        kn = 0
        print("Счётчик сброшен.")
    elif k == "0":
        print("Выход...")
        break
    else:
        print("Неизвестная команда")
