# Цикл for

# for (int i = 0; i <= 10; i++)
# for (int i = 0; i <= 10 && i > -10; i++)


# for i in 1, 2, 3:
#     print(i)

# range
# print(list(range(5)))
# for i in [0, 1, 2, 3, 4]:
#     print(i)

# range(n)=range(0, n, 1): [0, 1, 2, 3, .., n - 1] (количество равно n)
# range(n, 0, -1): [n, n - 1, n - 2,..., 2, 1]

for i in range(4, 13, 2):
    print(i, end=' ') # end='разделитель'

for i in range(5, 10):
    print(i) # 5 6 7 8 9