form = []
form.append(1)
form.append(2)
while True:
    i = len(form) - 1
    temp = form[i] + form[i-1]
    if temp > 100000000:
        break
    form.append(temp)

n = int(input())
for _ in range(n):
    x = int(input())

    ans = []
    max_index = 0

    print(f"{x} = ", end='')
    for i in range(len(form)):
        if x >= form[i]:
            max_index = i
        else:
            break

    for i in range(max_index, -1, -1):
        if x >= form[i]:
            ans.append(1)
            x-=form[i]
        else:
            ans.append(0)
            
    [print(a, end='') for a in ans]
    print(" (fib)")