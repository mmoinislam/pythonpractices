'''
#we can declare set in python 2 ways :

a = {'orange', 'banana', 'pear', 'apple'}

# or

#a = set('orange', 'banana', 'pear', 'apple')

b=set('one')  #item only cell
print(a)

'''



A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(A)


#blank set

A = set()
'''
#or
B ={}   #must set() use kora lagbe, only  {} eta diye hobe na
'''
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
A.add('pineapple')
print(A)


#add multiple item at one in set
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

#A.update('berry', 'grape')    this is wrong method 
A.update({'berry', 'grape'})
print(A)


#delete things
A.remove('apple')
print(A)
'''
#empty set a error dibe delete korte parbe na
A.remove('apple')
print(A)
'''
#if you dont want any error while deleting

A.discard('berry')
print(A)


A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(A)
A.pop()
print(A)
A.pop()
print(A)


#union set
A = {1, 2, 3, 4, 5}
B = {6, 7, 8}
c=A.union(B)

print(c)

#intersect in sets
A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 5, 6, 7}
D=A.intersection(B)
print(D)


#A set - B set / divide / diference
A = {1, 2, 3, 4, 5, 6}
B= {5, 6, 7, 8}
print(A.difference(B))
































