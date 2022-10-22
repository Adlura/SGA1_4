#if statement practice
from re import X

x = (input('please input your grade:'))
if type(x)==int:
    x = int (x)
    if x >= 70 and x<=100:
        print('A')
    elif x >=60 and x<=69:
        print('B')
    elif x >=50 and x<=59:
        print('C')
    elif x >=45 and x<=49:
        print('D')
    elif x >=40 and x<=44:
        print('E')
    else:
        print('failed')

else:
    print('Our program only accepts integer values')



print ('I will execute either way')

#Assignment: Research error handling using try and except statements