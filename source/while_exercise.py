''' 
ord('a') → gives the ASCII number of 'a'

chr(97) → gives the character 'a'
'''

i=1  
while i <= 5:
	letter = chr(ord('a') + i)
	print(letter)
	i+=1
print('--End of loop--')
print(chr(98)) 
print(ord('b'))