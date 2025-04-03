def digit_dlya_umnojenya(numbers, y=2):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num * y)
    return new_numbers

def l_funct(numbers, y=2):
    return list(map(lambda x: x * y, numbers))

def proverka_digit(s):
  return s.isdigit()

string_of_numbers = input("Введите список чисел через пробел: ")
numbers = []
for x in string_of_numbers.split():
    if proverka_digit(x):
        num = int(x)
        numbers.append(num)
    else:
        print("Обработка на ошибку - буквы в строке")
        numbers = []
        break

if numbers:
    str_mn = input("Введите множитель (прописано всё, кроме цифр - по умолчанию 2): ")
    if str_mn and proverka_digit(str_mn):
        y = int(str_mn)
    else:
        y = 2
    result_func = digit_dlya_umnojenya(numbers, y)
    result_l = l_funct(numbers, y)
    print(f"Результат (функция): {result_func}")
    print(f"Результат (Лямбда-функция): {result_l}")
