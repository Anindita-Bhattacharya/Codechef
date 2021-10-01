# cook your dish here
t=int(input())
while(t>0):
    m,n=map(int,input().split())
    a=list(input().split())
    c=[]
    for i in range(n):
        b=list(input().split())
        c=c+b[1:] 
    for i in a:
        if i in c:
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print("")
    t=t-1
    
