def sum_even ():
    sum = 0
    i = 0
    while i < 101:
        if i%2 == 0:
            sum += i
        i += 1
    return sum


def squares ():
    return [x * x for x in [1, 3, 5, 7, 9]]


def is_positive(num):
    return num <= 0


print(f"Сумма четных чисел в интервале от 1 до 100: {sum_even()}")
print(f"Квадраты нечетных чисел, поcтроенные методом генератора списков: {squares()}")
user_num = 1
count_of_positive = -1
while not is_positive(user_num):
    count_of_positive +=1
    user_num = int(input("Введите положительное число: "))
print(f"Введено положительных чисел: {count_of_positive}")

