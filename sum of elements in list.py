#sum of elements in list
li=[]#li=list()
sum1=0
n=int(input("enter the number:"))
for i in range(n):
   print('-'*10)
   x=int(input("enter the list element:"))
   li.append(x)
print(li,end='')
for i in li:
    sum1 +=i
print("sum of elements in list: ",sum1)
