# cook your dish here
t=int(input())
while(t>0):
    m,n,o=map(float,input().split())
    if m>50 and n<0.7 and o>5600:
        print("10")
    elif m>50 and n<0.7:
        print("9")
    elif  n<0.7 and o>5600:
        print("8")
    elif m>50 and o>5600:
        print("7")
    elif m>50 or n<0.7 or o>5600:
        print("6")
    else:
        print("5")
    t=t-1
