for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    f = 1
    k = 0
    b.append(a[0])
    print(1, end='')
    for i in range(1, n):
        if f:
            if a[i] >= b[k]:
                print(1, end='')
                b.append(a[i])
                k += 1
            elif a[i] <= b[0]:
                print(1, end='')
                b.append(a[i])
                k += 1
                f = 0
            else:
                print(0, end='')
        else:
            if a[i] >= b[k] and a[i] <= b[0]:
                print(1, end='')
                b.append(a[i])
                k += 1
            else:
                print(0, end='')
    print()
