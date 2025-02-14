n=int(input())
a=int(input())
b=int(input())
print(a,b)
for i in range (2,n+1):
   c=a+b
   print(c,end="")
   a=b
   b=c
