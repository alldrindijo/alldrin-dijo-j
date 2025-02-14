a=int(input('enter english mark:'))
b=int(input('enter tamil mark:'))
c=int(input('enter maths mark:'))
d=int(input('enter physics mark:'))
e=int(input('enter chemistry mark:'))
average=a+b+d+e/5
if(average<35):
    print('additional class is required')
else:
    print('you are good to go')
