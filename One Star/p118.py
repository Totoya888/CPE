dx = {"N": 0, "E": 1, "S": 0, "W": -1}
dy = {"N": 1, "E": 0, "S": -1, "W": 0}
right = {"N": "E", "E": "S", "S": "W", "W": "N"}
left = {"N": "W", "W": "S", "S": "E", "E": "N"}

x, y = map(int, input().split())


def cout(x, y, d, fall: bool):
    if fall:
        print(f"{x} {y} {d} LOST")
    else:
        print(f"{x} {y} {d}")


while True:
    try:
        t = list(input().split())
        cx, cy, d = int(t[0]), int(t[1]), t[2]
        com = input()
        li = []
        drop = False
        for c in com:
            print(f"x{cx} y{cy} {d}")
            if c == 'F':
                cx += dx[d]
                cy += dy[d]
                if cx > x or cy > y or cx < 0 or cy < 0:
                    skip = False
                    for l in li:
                        if cx - dx[d] == l[0] and cy - dy[d] == l[1]:
                            print("SKIP")
                            skip = True
                            break
                    if skip:
                        continue
                    temp = (cx - dx[d], cy - dy[d])
                    li.append(temp)
                    print(f"LIST: {li}")
                    drop = True
                    break
            else:
                if c == 'L':
                    d = left[d]
                elif c == 'R':
                    d = right[d]
        if drop:
            cout(cx - dx[d], cy - dy[d], d, True)
        else:
            cout(cx, cy, d, False)
    except:
        break

'''
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
'''
'''
1 1 E
3 3 N LOST
2 3 S
'''
