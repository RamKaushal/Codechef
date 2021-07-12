for i in range(int(input())):
    d,x,y,z = map(int,list(input().split(" ")))
    m1 = x*7
    m2 = y*d+(7-d)*z
    print(max(m1,m2))
