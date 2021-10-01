m,n=map(int,input().split())
count=0
for i in range(m):
    a=int(input())
    if a%n==0:
        count=count+1
print(count)
