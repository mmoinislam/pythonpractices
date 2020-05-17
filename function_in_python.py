#function is like a machine
# ex: rice cutter
#peddy (ধান ) is parameter
#machine makes it rice , which is function return or result.

#in python function is a organized and reusable code block .

#function is mainly 2 types :
# 1) is built-in , 2) user-defined


'''        parameter             |    returns 
abs()       int/float number           পরমমান or absolute  value
all()       iterable                    if itrable item is true returns all
any()       iterable                    if any one is true , otherwise false
enumerate()  iterable (starts with 0)   starts from 0,as tuple
'''

#function abc :


def moin():
    
    #hijibiji codes
    
    print('life is gangbanged')
    return
moin()

'''
def _love(nameyourlove):
    
    #shit things
    c=input()

    print(c)
    return
_love()
'''
'''
def print_name(hername):

    print('her name is ' , hername)
    return
print_name('nova')



#another way :
def print_my_name(myname):
    # This will print the given name
    print('The given name is', myname)
    return

name = 'Moin'

print_my_name(name)
'''

'''
#return type :

def mathes(a,b,c):
    return a+b+c
temp = mathes(1,2,3)
print(temp)

def hello():
    print("Hello World!")
hello()
'''

#function parameter or argument:
#4 types

'''
#Required argument

def add(a,b,c):
    return a+b+c
temp=add(2,4,3)
print(temp)
'''

'''
def adds(a,b,c):
    return a+b+c
temp=adds(2,4)    #error cz c er man dei nai 
print(temp)
'''

'''
#Keyword argument

def mini(a,b,c):
    return a+b+c
temp = mini(c=1,b=4,a=0)
print(temp)

#Default argument

def siri(a,b,c=4):
    return a+b+c
temp = siri(1,3)
print(temp)

# alternative :

def add(a, b, c=3):     #passed new value for c is 22
    return a+b+c
temp = add(1, 2, 22)
print(temp)
'''

'''
#Variable-length argument    
def minus(*args):
    print(type(args))        #ফাংশনের যেকোন প্যারামিটারের আগে একটা অ্যাসটেরিস্ক * চিহ্ন দিলে সেটা আনলিমিটেড ভ্যালু হোল্ড করতে পারে।
                             #জেনে রাখা ভাল, এই প্যারামিটারটা একটা টাপল তৈরি করে সবগুলো ভ্যালু হোল্ড করে। পরে একটা
                             #for লুপ চালিয়ে আমরা সবগুলো ভ্যালু অ্যাক্সেস করতে পারি। 
    tmp = 0
    for number in args:
        tmp = tmp + number
    return tmp
tmp = minus(1+2+22+12+17+21+98)
print(tmp)

'''


#যদি আমরা কি-ওয়ার্ড আর্গুমেন্ট পাস করতে চাইতাম?
#তখন প্যারামিটারের আগে দুইটা অ্যাসটেরিস্ক * চিহ্ন দিতে হত। এটাকে কীওয়ার্ডেড (keyworded) ভ্যারিয়েবল লেংথ আর্গুমেন্ট বলা হয়।
# এই প্যারামিটারটা একটা ডিকশনারি তৈরি করে সবগুলো ভ্যালু হোল্ড করে।

'''
def minion(**kwargs):
    print(type(kwargs))
    tmp = 0
    for key in kwargs:
        tmp = tmp + kwargs[key]
    return tmp
tmp = minion(a=1,b=2,c=3,d=4)
print(tmp)

'''


'''
#recursion , when a function call itself :

def counter(num):
    print(num)
    num+=1
    counter(num)
counter(1)   #this line calls the function

'''

'''
#factorial :
print('Please input your number:')
number = int(input())
temp = number

while number > 1:
    number -= 1
    temp = temp*number

if temp == 0:
    print(1)
else:
    print(temp)



    
'''

'''
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print('Please input your number:')
number = int(input())
print(factorial(number))

# one lin function using lambda

sum = lambda a, b: a+b
print(sum(10,20))
print((lambda a,b : a+b)(10,20))


#map () is a built in function :

my_list = [2, 3, 4, 5, 6, 7]

def sqre(x):
    return x*x
new_list = map (sqre,my_list)
print(new_list)
print(list(new_list))


#another type built in :
a, b = map(int, input().split())
print(type(a))
print(type(b))
print(a+b)


#filter function filter()
my_list = [2, 3, 4, 5, 6, 7]

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

new_list = filter(is_even, my_list)
print(new_list)
print(list(new_list))



#ছোটবেলায় স্কুলে আমরা গ.সা.গু বা গরিষ্ঠ সাধারণ গুণনীয়কের অনেক সমস্যা সমাধান করেছি। ইংরেজিতে একে বলা হয়, GCD বা Greatest Common Divisor। দুটি সংখ্যার GCD বের করার জন্য একটি ফাংশন লিখতে হবে।
def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

print("Please input two integers:")
a, b = map(int, input().split())
print(gcd(a, b))



#ল.সা.গু বা লঘিষ্ঠ সাধারণ গুণিতকই বা বাদ থাকবে কেন? ইংরেজিতে একে বলা হয় LCM বা Least Common Multiple। দুটি সংখ্যার LCM বের করার জন্য একটি ফাংশন লিখতে হবে।

def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)

print("Please input two integers:")
a, b = map(int, input().split())
print(lcm(a, b))

#ইউজার একটি পূর্ণসংখ্যা ইনপুট দেবে। আমাদের বলতে হবে সেটি মৌলিক (Prime) সংখ্যা, নাকি যৌগিক (Composite) সংখ্যা।
#০ আর ১ ব্যতীত যেসব সংখ্যা ওই সংখ্যা আর ১ ব্যতীত অন্য কোনো সংখ্যা দিয়ে নিঃশেষে বিভাজ্য হয় না, তাদের মৌলিক সংখ্যা বলে।

def is_prime(n):
    if n <= 1:
        raise ValueError('The number must be greater than 1.')
    elif n <= 3:
        return True
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    else:
        i = 5
        while (i * i) <= n:
            if (n % i) == 0 or (n % i+2) == 0:
                return False
            i = i + 6
        return True

print('Please input your number:')
number = int(input())

if is_prime(number):
    print(number, 'is a prime number.')
else:
    print(number, 'is a composite number.')


#find big
    larger_value = get_larger(23, 32) # Function is done with working and returned something here
larger_value = 32

'''


#module

#মডিউল হচ্ছে কিছু কোডের সমষ্টি যেখানে বেশ কিছু ফাংশন, ভ্যারিয়েবল বা ডাটা থাকে এবং
#যেগুলোকে অ্যাক্সেস করে প্রয়োজনে আরেকটি পাইথন প্রোগ্রামে ব্যবহার করা যায়। পাইথনের অনেক অনেক বিল্ট-ইন মডিউল আছে
#যেগুলোতে অনেক অনেক প্রয়োজনীয় ফাংশন যুক্ত করাই আছে। নিজেদের জন্য কোন প্রোগ্রাম লেখার সময় চাইলে সেই মডিউল গুলো থেকে
#উক্ত ফিচার গুলো ব্যবহার করা যায়।



import random

value = random.randint(1, 100)
print(value)



#other example:

from math import pi, sqrt

print(pi)
print(sqrt(25))

#
from math import sqrt as square_root

print(square_root(25))




#এখানে জমা থাকা মডিউল গুলোকে নিজের কম্পিউটারে ইন্সটল করার সবচেয়ে সহজ পদ্ধতি হচ্ছে pip নামের একটি টুল বা প্রোগ্রাম ব্যবহার করা।
#যদি  আপনি পাইথনের অফিসিয়াল সাইট থেকে পাইথনের আপডেটেড ভার্সন ডাউনলোড করে ইন্সটল করে থাকেন তাহলে এই টুলটিও সাথে ইন্সটল হয়ে থাকার কথা।

#প্রথমে টার্মিনাল ওপেন করতে হবে (উইন্ডোজ হলে কমান্ড প্রম্পট) এবং নিচের কমান্ডটি ইস্যু করতে হবে,

#       pip install LIBRARY_NAME

'''
exmaple :

pip install -U scikit-learn


'''





































































