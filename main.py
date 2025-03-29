def sum_even ():
    return sum([x for x in range(101) if x % 2 == 0])


def squares ():
    return [x * x for x in range(10) if x % 2 == 1]


def positive_counts():
    user_num = 1
    count_of_positive = -1
    while user_num > -1:
        count_of_positive += 1
        user_num = int(input("Введите положительное число: "))
    print(f"Введено положительных чисел: {count_of_positive}")

print(f"Сумма четных чисел в интервале от 1 до 100: {sum_even()}")
print(f"Квадраты нечетных чисел, поcтроенные методом генератора списков: {squares()}")
positive_counts()



