# Write content to a file 
file_obj=open("samplefile.txt","w")
file_obj.write("The content starts up here\n")
file_obj.write("Here is another content\n")
file_obj.write("Finally it ends-up")
file_obj.close()

print("\n\n")

# Add content in the list and write in file 
list1=['The content starts up here',
       'Here is another content',
       'Finally it ends-up']
file_obj1=open("samplefile2.txt","w")
print(file_obj1.writelines(list1))
file_obj1.close()

# Read content from a file
file_obj2=open("samplefile.txt","r")
print(file_obj2.read(10))
print(file_obj2.read(15))
print(file_obj2.readlines())
file_obj2.close() 

# Add complex data using pickle module 
import pickle
name={'1':'Udesh','2':'Kumar','3':'Aadhithya'}
department={'CSE':'REC','IT':'CIT','CS':'SRM'}

pickle_file=open('samplefile3.txt','wb')
pickle.dump(name,pickle_file)
pickle.dump(department,pickle_file)
pickle_file.close()

# Unpickle to load content
import pickle
pickle_accessfile=open('samplefile3.txt','rb')
d1=pickle.load(pickle_accessfile)
d2=pickle.load(pickle_accessfile)
print(d1,"\n\n",d2) 


