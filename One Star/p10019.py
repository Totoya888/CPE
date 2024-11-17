def toDec(n: int):
    cnt = 0
    while True:
        if n > 0:
            if n % 2 == 1:
                cnt += 1
            n //= 2
        else:
            break
    return cnt

def toHex(n: int):
    s = str(n)
    cnt = 0
    for k in s:
        j = int(k)
        cnt += toDec(j)
    return cnt

n = int(input())
for _ in range(n):
    m = int(input())
    print(toDec(m), end=' ')
    print(toHex(m))

'''
39 19
8 4 2 1
'''