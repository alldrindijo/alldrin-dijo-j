n=int(input())
val=0
while(n):
    rem=n%10
    val=val+rem
    n//=10
    print(val)
    
