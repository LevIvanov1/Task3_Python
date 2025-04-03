def plus(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Вводим только число, не букву.")
        return None
    return x + y

def minus(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Вводим только число, не букву.")
        return None
    return x - y

def multiplication(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Вводим только число, не букву.")
        return None
    return x * y

def division(x, y, division_type="обычное"):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Вводим только число, не букву.")
        return None
    if y == 0:
        print("Делить на нуль нельзя")
        return None

    if division_type == "обычное":
        return x / y
    elif division_type == "целочисленное":
        return x // y
    elif division_type == "остаток":
        return x % y
    else:
        print("Так нельзя.")
        return None

def exponentiation(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Вводим только число, не букву.")
        return None
    return x ** y

def factorial(n):
    if not isinstance(n, int):
        print("Целое число должно быть")
        return None
    if n < 0:
        print("Неотриц. число")
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x, iterations=10):
    if not isinstance(x, (int, float)):
        print("Число!")
        return None

    result = 0
    for i in range(iterations):
        numerator = (-1)**i * x**(2*i + 1)
        denominator = factorial(2*i + 1)
        if denominator is None:
            return None
        result += numerator / denominator
    return result

def median(numbers):
    if not isinstance(numbers, list):
        print("Должен быть списком.")
        return None
    for num in numbers:
        if not isinstance(num, (int, float)):
            print("Вводим только число, не букву.")
            return None
    if not numbers:
        print("Обязательно введите число, иначе никак")
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_numbers[n // 2]

def invalid_digit(s):
    if s.replace('.', '', 1).isdigit():
        return True
    else:
        return False

while True: # try-except вполне здесь уместен
    print("\nВозможные операции в калькуляторе:")
    print("1. Складываем;")
    print("2. Вычитаем;")
    print("3. Умножаем;")
    print("4. Делим;")
    print("5. Возводим в степень;")
    print("6. Факториал;")
    print("7. Синус;")
    print("8. Медиана;")
    print("exit")

    choice = input("Выберите операцию (от 1 до 8) или exit: ")

    if choice == 'exit':
        break
    if not choice.isdigit():
        print("Только цифры или вы ничего не ввели!")
        continue
    choice = int(choice)

    if not 1 <= choice <= 8:
        print("Выберите операцию числом! От 1 до 8 или 'exit'.")
        continue
    if choice in (1, 2, 3, 4, 5):
        num1_str = input("Введите первое число: ")
        if not invalid_digit(num1_str):
            print("Введите число ещё раз.")
            continue
        num1 = float(num1_str)

        num2_str = input("Введите второе число: ")
        if not invalid_digit(num2_str):
            print("Число!")
            continue
        num2 = float(num2_str)
        result = None

        if choice == 1:
            result = plus(num1, num2)
        elif choice == 2:
            result = minus(num1, num2)
        elif choice == 3:
            result = multiplication(num1, num2)
        elif choice == 4:
            print("Выберите тип деления:")
            print("1. Обычное")
            print("2. Целочисленное")
            print("3. Остаток")
            division_choice = input("Введите, что указно сверху: ")
            if division_choice == "1":
                division_type = "обычное"
            elif division_choice == "2":
                division_type = "целочисленное"
            elif division_choice == "3":
                division_type = "остаток"
            else:
                print("Выбор не из предложенного списка, либо не ввели")
                continue

            result = division(num1, num2, division_type)
        elif choice == 5:
            result = exponentiation(num1, num2)

        if result is not None:
            print("Результат: ", result)
    elif choice == 6:
        num_str = input("Введите целое число для вычисления факториала: ")
        if not num_str.isdigit():
            print("Числом.")
            continue
        num = int(num_str)
        result = factorial(num)
        if result is not None:
            print(">>>", result)
    elif choice == 7:
        num_str = input("Введите число для вычисления Sin: ")
        if not invalid_digit(num_str):
            print("Число")
            continue
        num = float(num_str)
        result = sin(num)
        if result is not None:
            print("Результат: ", result)
    elif choice == 8:
        numbers_str = input("Введите список чисел через пробел: ")
        numbers = []
        numbers_valid = True
        for s in numbers_str.split():
            if invalid_digit(s):
                numbers.append(float(s))
            else:
                print("Числа вводим через пробел.")
                numbers_valid = False
                break
        if numbers_valid:
            result = median(numbers)
            if result is not None:
                print("Результат: ", result)
