salary=int(input('enter the salary'))
age=int(input('enter the age '))
if(salary>=20000 and age<=25):
     loan=int(input('enter your loan amount'))
     print("loan amount:",loan)
if(loan<=50000):
              print('your eligible')
else:
    print('not eligible for loan')
