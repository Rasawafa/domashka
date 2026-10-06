N = 4
Z = 2
contacts = {"Анна": "+7991234567"}

while True:
    cmd = input("Команда: ").strip().lower()

    if cmd == "список":
        a = 1
        for name in contacts:
            phone = contacts[name]
            mask = phone[:N] + "***" + phone[-Z:]
            print(f"{a}. {name} - {mask}")
            a += 1

    elif cmd == "поиск":
        q = input("Найти: ").strip()
        f = False

        for name in contacts:
            phone = contacts[name]
            if q in phone:
                mask = phone[:N] + "***" + phone[-Z:]
                print(f"{name} - {mask}")
                f = True

        if not f:
            print("Контакты не найдены")

    elif cmd == "выход":
        break

    else:
        print("Команды: список, поиск, выход")
