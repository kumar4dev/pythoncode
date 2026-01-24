# range function start,stop 
for y in range(2,8): 
    if y % 2==0:
        print(y) 

print('\n')

# range function using start,stop,step 
for yet_another_y in range(2,10,2): 
    print(yet_another_y) 

print('\n')

'''
Exercise: 
Number div by 3 and 5 'FizzBuzz'
Number div by 3 'Fizz'
Number div by 5 'Buzz'
Print rest of the number as it is 
'''
for x in range(1,16):

    if x % 3 == 0 % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
        continue
    else:
        print(x)
print('\n')


