kn = 0  

print("=== Учёт книг [2] ===")

while True:
    print()
    print("Меню:")
    print("1 - Выдать книгу")
    print("2 - Показать, сколько книг выдано")
    print("3 - Сбросить счётчик")
    print("4 - Вернуть книгу")
    print("0 - Выход")

    er = input("Введите команду: ")

    if er == "1":
        kn = kn + 1
        print("Книга выдана. Выдано всего:", kn)
    elif er == "2":
        print("Книг выдано:", kn)
    elif er == "3":
        kn = 0
        print("Счётчик сброшен.")
    elif er == "4":
        if kn == 0:
            print("Нет выданных книг")
        else:
            kn = kn - 1
            print("Книга возвращена. Выдано всего:", kn)
    elif er == "0":
        print("Выход...")
        break
    else:
        print("Неизвестная команда")
        kn = 0
