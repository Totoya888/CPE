n = int(input())
for _ in range(n):
    a = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
                cnt += 1
            
    print(f"Optimal train swapping takes {cnt} swaps.")
    

'''
3
3
1 3 2
4
4 3 2 1
2
2 1
'''

'''
3421
3241
3214
2314
2134
1234
'''

'''
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps.
'''