n,f = map(int,input().split())
sold=0
sell_out=[]

for i in range(n):
    a,b = map(int,input().split())
    c = min(a,b)
    d = min(2*a,b)
    sold+=c
    sell_out.append(d-c)

sell_out.sort()
for i in range(n-1,n-f-1,-1):
    sold += sell_out[i]

print(sold)

