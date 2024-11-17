flag = False
while True:
    try:
        s = input()
        for c in s:
            if c == '"':
                flag = not flag
                if flag:
                    print("``", end='')
                else:
                    print("''", end='')
            else:
                print(c, end='')
        print()

    except:
        break

'''
"To be or not to be," quoth the Bard, "that
is the question".
The programming contestant replied: "I must disagree.
To `C' or not to `C', that is The Question!"
'''