#Iterator means read item one by one
'''
a = ['onion', 'potato', 'ginger', 'cucumber']
print(type(a))
for item in a:
    print(item)
'''

'''
#tuple or set iterate :
a = {'name' : 'MD. Maksudur Rahman Khan', 'nickname' : 'Maateen', 'email' : 'maateen@outlook.com', 'phone' : '01711223344'}
print(a)
print(type(a))
for item in a:
    print(item)
'''

'''
#string :

a='python'
for letter in a:
    print(letter)

'''

'''
#range :

range(5)
print(list(range(5)))

#5-21 print:
range(5,21)
print(list(range(5,21)))

#5, 7, 9, 11

range(5,21,2)
print(list(range(5,21,2)))
'''

'''
#for loop:
for number in range(1,11):
    print(number)


'''


'''
#use break :

for n in range(1,10):
    if n == 5:
        break
    print(n)
'''
'''
# use continue :

for number in range(1, 11):
    if number == 5:
        continue
    print(number)

'''
# pass command:

for number in range(1, 11):
    if number == 5:
        pass
    print(number)


#for loop using else :

for n in range(0, 11):
    print(n)
    n = n + 1
else:
    print('The loop is over.')






























