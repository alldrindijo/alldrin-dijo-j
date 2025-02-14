def val(n):
    while(n):
        rem=n%10
        print(rem,end="")
        n//10
n=int(input())
val(n)
