def to_hexadecimal(number):
    if number == 0:
        return '0'  # Обработка случая, когда число равно 0

    hexadecimal_digits = '0123456789ABCDEF'  # Возможные цифры в шестнадцатеричном представлении
    hexadecimal_string = ''  # Инициализация пустой строки для шестнадцатеричного представления

    while number > 0:
        remainder = number % 16  # Остаток от деления на 16
        hexadecimal_string = hexadecimal_digits[
                                 remainder] + hexadecimal_string  # Добавляем соответствующую цифру в начало строки
        number //= 16  # Деление на 16 без остатка

    return hexadecimal_string


# Получение ввода от пользователя
number = int(input("Введите целое число: "))

# Вызов функции и вывод результата
hexadecimal = to_hexadecimal(number)
print("Шестнадцатеричное представление числа (наша функция):", hexadecimal)

# Проверка с использованием встроенной функции hex()
hexadecimal_builtin = hex(number)
print("Шестнадцатеричное представление числа (встроенная функция):", hexadecimal_builtin)

# Проверка: сравнение результатов
if hexadecimal == hexadecimal_builtin[2:].upper():
    print("Проверка успешна: оба представления совпадают.")
else:
    print("Проверка не пройдена: представления различаются.")
