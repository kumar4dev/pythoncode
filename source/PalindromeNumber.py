'''
Palindrome Number 
Sample Input: 2345612
Output: 2165432 is not a palindrome number

Even OR Odd Number 
Sample Input: 12388 
Output: 12388 is divisible by 2.EVEN 

'''
# function definition for Palindrome 
def isNum_Palin(num):
    temp=num
    rev=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if num==rev:
        print("Palindrome number")
    else:
        print(f"{rev} is not a palindrome number")

# function definition for even,odd number 
def isNum_evenodd(num):
    div_even=2
    div_odd=3
    if num%2==0: 
        print(f"{num} divisible by {div_even}.EVEN")
    elif num%3==0:
        print(f"{num} divisible by {div_odd}.ODD")
    else:
        print("PRIME NUMBER")  
        
num=int(input('Number '))
isNum_Palin(num)
isNum_evenodd(num)
        
