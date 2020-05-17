'''
#while loop

i=1
while i<=5:
    print(i)
    i=i+1

print('while loop ended here')

#infinite while loop

while 1==1:
    print("love is life")     #press control+c to stop the event



'''

'''
#while & break uses

i=0
while 1==1:
    print(i)
    i=i+1
    if i>=5:
        print("Breaking")
        break

print("ends")
'''

'''
#while - break & continue 

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")
'''

'''
#simple again:

n = 0
while n<=10:
    print(n)
    n=n+1

'''

# 1+2+3+4+…+100 = ? using while loop :

'''
n = 0
temp = 0
while n<=100:
    temp = temp + n
    n = n + 1
print(temp)
'''

'''
n = 100
temp = n*(n+1)
temp = temp/2
print(temp)
'''

'''
n = 1
while n <= 10:
    print(n)
    n = n + 1
else:
    print('The loop is over.')

'''

print('please , input the number: ')
number = int(input())
count=1
while count<=10:
    print(number,'x',count,'=',number*count)
    count+=1































    
