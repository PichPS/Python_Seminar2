# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))
x0 = 0
x1 = 1
x = 0
i = 2
while x < n:
    x = x0 + x1 # поиск следующего числа
    x0 = x1 # выполняем перекладывание. Мы нашли с Вами 3-е число, с помощью сумму 1-ого и 2-ого
    x1 = x # Теперь, чтобы найти сумму 4-ого, нужно сложить 2-ое и 3-е. Мы их сохраняем в переменные x0 и x1
    i += 1
    if x > n:
        i = 0
if i == 0:
    print(-1)
else:
    print(i)