numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_ = [2]
not_primes = []
len_list = int(len(numbers))

for i in range(3, (len_list+1), 2):
    for j in prime_:
        if j * j - 1 > i:
            prime_.append(i)
            break
        if i % j == 0:
            break
    else:
        prime_.append(i)
for i in range(2, (len_list + 1)):
    if i not in prime_:
        not_primes.append(i)


print('Простые ', prime_)
print('Не простые ', not_primes)