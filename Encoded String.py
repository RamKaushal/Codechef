from __future__ import print_function
for i in range(int(input())):
    si = int(input())
    k = str(input())
    decode = [int(i) for i in k]
    ans = []
    for j in range(0,len(k)//4):
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        for m in range(0,4):
            if decode[m] == 0:
                alpha = alpha[:len(alpha)//2]
            else:
                alpha = alpha[len(alpha)//2:]
        if si<=4:
            print(alpha)
        else:
            #print(alpha,end=' ')
            ans.append(str(alpha))
        decode = decode[4*(int(j)+1):]
    #ans1 = [str(i) for i in ans]
    print(*ans, sep='')