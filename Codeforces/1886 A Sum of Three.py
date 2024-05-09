def solve(m):
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            if x + y >= m or x == y:
                continue
            z = m - x - y
            if z == x or z == y:
                continue
            if x % 3 == 0 or y % 3 == 0 or z % 3 == 0:
                continue
            print("YES")
            print(f"{x} {y} {z}")
            return
    print("NO")
 
n = int(input())
for _ in range(n):
    m = int(input())
    solve(m)