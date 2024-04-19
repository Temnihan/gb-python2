from fractions import Fraction


def main():
    fraction1 = input("Введите первую дробь в формате a/b: ")
    fraction2 = input("Введите вторую дробь в формате a/b: ")

    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    # Вычисляем сумму и произведение вручную
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    product_numerator = numerator1 * numerator2
    sum_denominator = denominator1 * denominator2
    product_denominator = denominator1 * denominator2

    # Сокращаем дроби, если это возможно
    for i in range(2, min(sum_numerator, sum_denominator) + 1):
        while sum_numerator % i == 0 and sum_denominator % i == 0:
            sum_numerator //= i
            sum_denominator //= i

    for i in range(2, min(product_numerator, product_denominator) + 1):
        while product_numerator % i == 0 and product_denominator % i == 0:
            product_numerator //= i
            product_denominator //= i

    # Сумма и произведение дробей с помощью fractions для проверки
    fraction_sum = Fraction(sum_numerator, sum_denominator)
    fraction_product = Fraction(product_numerator, product_denominator)

    # Выводим результаты
    print("Сумма дробей (вручную):", f"{sum_numerator}/{sum_denominator}")
    print("Произведение дробей (вручную):", f"{product_numerator}/{product_denominator}")
    print("Сумма дробей (с использованием fractions):", fraction_sum)
    print("Произведение дробей (с использованием fractions):", fraction_product)


# Вызываем функцию main() для выполнения программы
main()
input()