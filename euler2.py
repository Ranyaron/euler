'''Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.'''

a = 1
b = 1
c = 0

while True:
    if a > 0:
        a += b
        b += a
        if b >= 4000000:
            break
        else:
            if (a % 2 == 0):
                c += a
            if (b % 2 == 0):
                c += b

print(c)
