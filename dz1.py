while True:
    print("Введите слово 'Выход' чтобы закончить работу программы.")

    a = input("Первое число: ").strip()
    if a.lower() == "выход":
        break
        
    o = input("Операция: ").strip()
    if o.lower() == "выход":
        break
        
    b = input("Второе число: ").strip()
    if b.lower() == "выход":
        break


    if not a.isdigit() and not b.isdigit():
        print("Ошибка, введите корректное число")
        continue
    n1=float(a)
    n2=float(b)

    if o == "+":
        otvet = n1 + n2
        print(f"Ответ: {otvet}")
    elif o == "-":
        otvet = n1 - n2
        print(f"Ответ: {otvet}")
    elif o == "*":
        otvet = n1 * n2
        print(f"Ответ: {otvet}")
    elif o == "/":
        if n2 == 0:
            print("Делить на ноль нельзя")
        else:
            otvet = n1 / n2
            print(f"Ответ: {otvet}")
    else:
        print("Операции: + - * /")

