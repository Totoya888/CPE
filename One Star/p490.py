li = []
max_len = 0
while True:
    try:
        s = input()
        li.append(s)
        max_len = max(max_len, len(s))
    except:
        break

for i in range(max_len):
    for j in range(len(li)):
        if len(li[-(j+1)]) <= i + 1:
            print(" ", end='')
        else:
            print(li[-(j+1)][i], end='')
    print()
"""
Rene Decartes once said,
"I think, therefore I am."
"""