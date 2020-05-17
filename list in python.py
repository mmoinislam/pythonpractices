

print('we will learn in python 4 types data basic structure system : \n list ,\n tuple ,\n set ,\n dictionary ')

a = []

a = ['life','sex','happy','pizza','travel','fun','sad','memory','humans']
print(a)
b = ['art','science',3.1416,94]
print(b)
#list access
#we will use index number
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
print(b[0],'\n')
print(b[1:5]) #for print index 1 to 5.
print(b[:3])    #print 3 to null or 0
print(b[3:])    #print 4 to last

#update list and its value

b[0]='rice'
print(b)

b[4] = 570
b[5] = 23486.4678
print(b)

#string er position a integer o int er jaigai string rcv kore naki check : 
b[2] = 343
b[4] = 'finger'
print(b)

'''
#insert new item to the list :
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
b[6] = 'new' #finds error
#for this reason use append()
'''
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
b.append('life')
print(b)

#insert in index position not at last 
b.insert(1, 'python')
print(b)


#insert many item at once :
b.extend(['cheat','rest','enjoy'])
print(b)


#more less code but insert many in a single command
b
b=b + ['a','b','c']
print(b)

#delete item from list by index number
del b[2]
print(b)

#delete item from list by value
b.remove('python')
print(b)

#delete last item from list
del b[-1]
print(b)

#delete last item from list
b.pop()
print(b)

#find length of list
print(len(b))


#find a single value how many times stored :
print(b.count('potato'))

#last er gula first a ante ba list ulta kore sajate :
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
b.reverse()
print(b)

#sorting or make sequencial list :
a = [8, 3, 5, 1, 6, 2, 9, 7, 0, 4]
print(a)
a.sort()
print(a)


b = ['b', 'c', 'a', ':', 'maateen']
print(b)
b.sort()
print(b)









