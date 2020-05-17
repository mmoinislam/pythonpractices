'''
#read
my_file = open('file.txt','r')
content = my_file.read()         #read kora data variable a anchi
print(content)
my_file.close()        #close() diye file ta close koresi


#write
my_file = open('file.txt','w')
my_file.write('My name is moin.')
my_file.close

#non existed file created
my_file = open('test.txt', 'w')
my_file.write('I am Maksudur Rahman Maateen.')
my_file.close()


#add txt in the end of the file :
my_file = open('test.txt', 'a')
my_file.write('I am from Bangladesh.')
my_file.close()

#another
my_file = open('test.txt', 'r')
content = my_file.read(5)
print(content)
content = my_file.read()
print(content)
position = my_file.tell()
print(position)
my_file.seek(0, 0)
content = my_file.read()
print(content)
my_file.close()


#other way
with open('test.txt', 'r') as my_file:
    content = my_file.read()
    print(content)
'''

try:
    file_to_work = open("Test.txt", "r")
    content = file_to_work.read()
    print(content)
finally:
    file_to_work.close()

'''

file_to_work_on = open("file.txt","r")
print(file_to_work_on)
file_to_work_on = open("D:/programming/python + oop/file.txt","r")
print(file_to_work_on)
print(file_to_work_on)
file_to_work = open("filename.txt", "w")
# do HERE whatever you like, with the file
# such as write new lines in it

# then close it
file_to_work.close()
'''

'''
with open("Test.txt") as f:
    print(f.read())
'''







