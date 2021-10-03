t=int(input())
a=[]
while(t>0):
    n=int(input())
    a.append(n)
    t=t-1
a.sort()
for i in a:
    print(i)
