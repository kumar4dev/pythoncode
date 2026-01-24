# Evaluate Grade 
M1=35 
M2=35 
M3=60 
print(M3) # 60
sub1=37
sub2=40
sub3=47
M3=34 
print(M3) # 34 

# Variable M3 defined first(that is M3=60) will get evaluated inside if condition 

if((sub1 >= M1 >= M2 >= M3) and(sub2 >= M1 >= M2 >= M3) and(sub3 >= M1 >= M2 >= M3)):
	total=sub1 + sub2 + sub3  
	avg = total/3  
	grade = avg / 10 
	if(grade >= 7 <= 10):
		print('Average=%.2f'%(avg)) 
		print('A') 

	elif(grade >= 4 <= 6.9): 
		print('Average=%.2f'%(avg))
		print('B')   

	else: 
		print('Average=%.2f'%(avg))
		print('C')
else: 
	print('RETRY')
