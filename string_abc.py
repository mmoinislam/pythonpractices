a='bangla'
print(a)
print('my fav. subject is :',a)

print('my language is :%s' %a)

number = 436.15757823658945
print(number)
print('%.2f' %number)

'''
a=int(input())
b=int(input())
print('the sum of %d and %d is: %d' %(a,b,a+b))
'''

#make all upper case

d='dolphine' 
print(d.capitalize()) #first letter of this string is captal
print(d.upper())

#make capital each letter from sentece
#use title function :  .title()


print('My name is Moin Islam'.title())



#make all lowwer case in a string:
print('BANGLA'.lower())
#or alternative code does as same as .lower is below

print("English".casefold())

#capital to small or small to cap
# swapcase()

print('ENGlish'.swapcase())

#find size of a string :
a='dhaka'
print(len(a))

#count same character in string : using :  .count()

print(a.count('a'))


print(a.count(a))

sentence = 'How can a clam cram in a clean cream can?'
print(sentence.count('c'))
print(sentence.count('c',5))
print(sentence.count('c',5,9))

#find() search a character
print('moin')
print(sentence.find('c'))
#result is 4 , which is index number

print(sentence.find('c', 5))
#result is 10

'''
a = "Bangladesh is my country"
print(a.find("x"))
print('\n')
print(a.index("x"))

#result find() returns -1 and index() shows error.
'''

sentence = 'How can a clam cram in a clean cream can?'
print(sentence.replace('c','d'))
#now we remove '?'
print(sentence.replace('?', ''))
sentence = 'How can a clam cram in a clean cream can?'
print(sentence.strip('?'))

#devide string upon white sppace sentence.split(' ') or 'any character'
print(sentence.split(' '))

print("First string" + ", " + "second string")
print('bangla'+''+'desh')
print('spam'*5)

msg = "My self score on PHP: {0}, Python: {1}, Java: {2}, Swift: {3}". format(6, 6.5, 5, 6)

print(msg)

print(", ".join(["apple", "orange", "pineapple"]))

print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("a, e, i, o, u".split(", "))











































