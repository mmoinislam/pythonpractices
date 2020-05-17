print('Please, input the number:')
number = int(input())

if number % 2 == 0:
    print('Even')
else:
    print('Odd')

#new one
    
print('Please, input the character:')
character = input()

if character >= 'a' and character <= 'z' :
    print('Lower Case')
elif character >= 'A' and character <= 'Z' :
    print('Upper Case')
else:
    print('Nothing')
#new one
    
a = int(input("Please input your a: "))
b = int
b = a
temp = a//1000
print(temp, '1000 Taka note(s).')
if temp > 0:
    a = a%1000
    b = a
else:
    a = b
temp = a//500
print(temp, '500 Taka note(s).')
if temp > 0:
    a = a%500
    b = a
else:
    a = b
temp = a//100
print(temp, '100 Taka note(s).')
if temp > 0:
    a = a%100
    b = a
else:
    a = b
temp = a//50
print(temp, '50 Taka note(s).')
if temp > 0:
    a = a%50
    b = a
else:
    a = b
temp = a//20
print(temp, '20 Taka note(s).')
if temp > 0:
    a = a%20
    b = a
else:
    a = b
temp = a//10
print(temp, '10 Taka note(s).')
if temp > 0:
    a = a%10
    b = a
else:
    a = b
temp = a//5
print(temp, '5 Taka note(s).')
if temp > 0:
    a = a%5
    b = a
else:
    a = b
temp = a//2
print(temp, '2 Taka note(s).')
if temp > 0:
    a = a%2
    b = a
else:
    a = b
temp = a//1
print(temp, '1 Taka note(s).')
