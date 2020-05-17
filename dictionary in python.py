a={}
b={}
print(type(a))

a= {'name':'moin','id':'03','year':'4th','phone':'01715301992'}
print(a)
print(a['id'])

#update value in dict
a['name']='moin islam'
print(a)

#update new item 
a['hometown']='dhaka'
print(a)

#use another dictionary in other one :
b = {'color':'red','food':'pizza','drinks':'coke'}
#a = a.update(b)
print(a.update(b))


#delete a type or item
del a['phone']
print(a)

#remove or clear all:
a.clear()
print(a)
'''
#delete the whole dictionary :
del a
print(a) #result error
'''
#full copy a dictionary
print(b)
e=b.copy()
print(e)

f=b.get('color')
print(f)

#does it have or not by true false
s='name' in b
print(s)

#items
v=a.items()
#see all keys
l=a.keys()
#see all values
t=a.values()
print(v)
print(l)
print(t)


























