t = int(input())
for i in range(0,t):
    n,k,d = map(int,input().split())
    total_problems = 0
    problems = list(input().split())
    probl = [int(i) for i in problems]
    total_problems = sum(probl)
    if total_problems<k:
        print("0")
    elif total_problems>=k:
        j = total_problems//k
        if j<d:
            print(j)
        else:
            print(d)
        