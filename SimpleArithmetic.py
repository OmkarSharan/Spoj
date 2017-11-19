t = int(input())
while t:
    t -= 1
    input()
    st = input().split()
    ans = int(st[0])
    for i in range(1, len(st), 2):
        if st[i] == "=":
            break
        op1 = int(st[i + 1])
        op = st[i]
        if op == "+":
            ans += op1
        if op == "-":
            ans -= op1
        if op == "*":
            ans *= op1
        if op == "/":
            ans //= op1
    print(ans)