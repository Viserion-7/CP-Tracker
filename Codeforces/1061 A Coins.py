n,s=map(int,input().split())
ans =s//n
if s%n>0:
    ans+=1
print(ans)