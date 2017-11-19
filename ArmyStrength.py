t = int(input())
while t:
    input()
    t -= 1
    ng, nm = map(int, input().split())
    ngAS = []
    nmAS = []
    ngAS = list(map(int, input().split()))
    nmAS = list(map(int, input().split()))
    god = max(ngAS)
    Mgod = max(nmAS)
    if god >= Mgod:
        print("Godzilla")
    elif god < Mgod:
        print("MechaGodzilla")
    else:
        print("uncertain")


