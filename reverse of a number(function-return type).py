def val(n):
    rev=0
    while(n):
        rem=n%10
        rev+rev*10+rem
        n//=10
    return rev
n=int(input())
print(val(n))
