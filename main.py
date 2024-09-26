N = int(input("Введіть число N: "))

if 1 < N < 9:
    for i in range(1, N + 1):
        for j in range(N, N - i, -1):
            print(j, end=" ")
        print()
else:
    print("N повинно бути більше за 1 та менше за 9.")