t=int(input())
while(t>0):
    a=[]
    A,B,C=map(int,input().split())
    a.append(A)
    a.append(B)
    a.append(C)
    a.sort()
    print(a[-2])
    t=t-1
    
