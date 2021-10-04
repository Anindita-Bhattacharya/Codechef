# cook your dish here
t=int(input())
while(t>0):
    A,B=map(int,input().split())
    if A>B:
        print(">")
    elif A<B:
        print("<")
    elif A==B:
        print("=")
    t=t-1
