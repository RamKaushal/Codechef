t = int(input())
for i in range(0,t):
    n,m = map(int,input().split())
    jack = list(input().split())
    john =list(input().split())
    int_jack = [int(i) for i in jack]
    int_john = [int(i) for i in john]
    jsum = sum(int_jack)
    josum = sum(int_john)
    int_jack.sort()
    int_john.sort(reverse = True)
    count = 0
    for i in range(0,min(n,m)):
        int_jack[i],int_john[i] = int_john[i],int_jack[i]
        josum = sum(int_jack)
        jsum = sum(int_john)
        count += 1
        if josum>jsum:
            break
        else:
            continue
    print(count)
            
            
        