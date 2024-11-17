n = int(input())

s = ""
for _ in range(n):
    s += input()

dic = {}
for i in range(26):
    dic[chr(ord('A') + i)] = 0

for c in s:
    if c.isalpha():
        ch = c.upper()
        dic[ch] += 1

maxx = 0
max_key = ""
while len(dic):
    maxx = 0
    for key, value in dic.items():
        if value > maxx:
            maxx = value
            max_key = key
    if maxx == 0:
        break
    print(f"{max_key} {maxx}")
    dic.pop(max_key)

"""
3
This is a test.
Count me 1 2 3 4 5.
Wow!!!! Is this question easy?
"""