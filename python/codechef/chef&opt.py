n=int(input())
for i in range(n):
    x,y = map(int,input().split())
    if(x<y):
        print("<")
    if(x>y):
        print(">")
    if(x==y):
        print("=")