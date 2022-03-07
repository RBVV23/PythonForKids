# Описание: Один известный математик однажды придумал числа, которые
# так и называются теперь - числа Фибоначчи. А работает это так:
# Первые два числа этой последовательности - это 1 и 1. А каждое
# следующее число - сумма двух предыдущих. Вот начало этой
# последовательности: 1 1 2 3 5 8 13 21

# Задание: заведи массив длины 10 и сгенерируй туда первые 10 чисел Фиббоначчи.
# А затем выведи их все на экран.

fibo = [1, 1]
for i in range(2, 10, 1):
    ham = fibo[i-2] + fibo[i-1]
    fibo.append(ham)

print('Последовательность Фибоначчи: ', fibo)
