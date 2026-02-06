'''
Errors occur during the
runtime of a program is known as
exception. Techniques to handle such
exceptions are exception handling
'''

'''
div error. Cannot divide number by denominator.
In case numerator answer returns 0
'''
try:
    num=int(input('Number '))
    res=num/0
except(ValueError,ZeroDivisionError) as arg:
    print(arg) 
else:
    print(res)
finally:
    print('--End of the program--')
