# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_ = []
not_primes = []

for i in numbers:
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            not_primes.append(i)
            break
    if i not in not_primes:
        prime_.append(i)
prime_.remove(1)
print('Простые ', prime_)
print('Не простые ', not_primes)






