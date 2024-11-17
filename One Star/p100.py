def alg(n):
    cnt = 0
    while True:
        cnt += 1
        if n == 1:
            break
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
    return cnt


while True:
    try:
        a, b = map(int, input().split())
        print(f"{a} {b}", end=" ")
        if a > b:
            a, b = b, a
        result = 0
        for i in range(a, b+1):
            m2 = alg(i)
            result = max(m2, result)
        print(result)
    except:
        break
