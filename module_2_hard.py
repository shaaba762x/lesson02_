import random
def ran_num():
    num1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    num_ = random.choice(num1)
    return num_

result = ''
num_ = ran_num()
for i in range(1, num_):
    for j in range(1, num_):
        if num_ % (i + j) == 0 and i < j:
            result += str(i) + str(j)
print(f'Шифр для числа {num_}: {result}')
