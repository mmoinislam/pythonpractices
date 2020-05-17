'''
with open('tt.txt', 'r') as my_file: #no file name tt.txt
    content = my_file.read()
    print(content)

'''

'''
#so

try:                                         #normal codes will be in try bloxck
    with open('tt.txt','r') as my_file:
        content = my_file.read()
        print(content)
except:                                        #errors code handle will be here
    print('file doesnt exist')


'''

'''
try:
    with open('tt.txt', 'r') as my_file:
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')

print('Made by Maateen.')

try:
    my_list = []
    print(my_list[0])
except IndexError as e:
    print(e)

'''

'''
try:
    my_file = open('tt.txt')
    content = my_file.read()
    i = int(content.strip())

except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error!")

'''


'''
#চাইলে সবগুলো এররকে একটা except ব্লকে সেটেল করে দিতে পারতাম


try:
    my_file = open('tt.txt')
    content = my_file.read()
    i = int(content.strip())

except (IOError, ValueError):
    pass
'''


'''
#try … except … else

try:
    a = 5
    b = 8
    print(a + b)
except ValueError as e:
    print(e)
else:
    print('There is no exception.')

'''

'''
#try … except … finally

try:
    with open('tt.txt', 'r') as my_file:
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')
finally:
    print('To be or not to be that is the question.')
'''

'''
#raise exception (built in error )

try:
    raise NameError('Hey! It is a custom error message.')
except NameError as e:
    print(e)

'''
'''
a = 2500
b = 0

print(a/b)
print("I did it")
'''

'''
try:
    a = 1000
    b = int(input("Enter a divisor to divide 1000: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")

'''


'''
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Type or value error occurred")
    

উপরের প্রোগ্রামে ট্রাই ব্লকে দুই রকম অঘটন ঘটতে পারে।
variable কে 2 দিয়ে ভাগ না করে শূন্য দিয়ে ভাগ করা হতে পারতো এবং
সেক্ষেত্রে ZeroDivisionError এক্সেপশন তৈরি হত। আবার ট্রাই ব্লকের দ্বিতীয় স্টেটমেন্ট
যেখানে একটি ইন্টিজারের সাথে স্ট্রিং কে যোগ করে প্রিন্ট করার চেষ্টা করা হয়েছে, সেখানে।
এই উদাহরণে এখানেই এক্সেপশন তৈরি হচ্ছে। আর তাই TypeError এক্সেপশন তৈরি হচ্ছে।
কিন্তু আমরা সেটা সঠিকভাবে হ্যান্ডেল করেছি আর তাই প্রোগ্রাম হুট করে বন্ধ না হয়ে
বরং সুন্দর ভাবে আমাদের নির্ধারিত একটি প্রিন্ট স্টেটমেন্ট
print("Type or value error occurred") এক্সিকিউট করেছে।
'''

'''
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

'''

'''
যদি এমন দরকার হয় যে, যতই এক্সেপশন তৈরি হোক না কেন কিছু কোডকে রান করানো দরকার,
তখন finally স্টেটমেন্ট ব্যবহার করা হয়। try, except ব্লকের নিচে finally ব্লক ব্যবহার
করতে হয়। try বা except ব্লকের কোড রান হবার পর এই finally ব্লকের মধ্যে থাকা কোড
গুলো রান হবেই। একটি উদাহরণ দেখি :
যদি finally ব্লকের আগে এমন কোন এক্সেপশন তৈরি হয় যাকে সঠিক ভাবে হ্যান্ডেল করা হয় নাই,
সে অবস্থাতেও finally ব্লকের কোড রান হবে। যেমন -
'''

'''
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

'''

'''
try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print(unknown_var)
finally:
   print("This is executed last")

'''


#raise Exception :

'''

print("Hello")
raise NameError('HiThere')

'''

'''

raise TypeError

'''

'''
try:
    num = 5 / 0
except:
    print("Custom message about an error!")
    raise

'''
'''
methods used to find error types :








#FileNotFoundError
#ImportError
#IdentationError
#IndexError
#keyboardInterruption
#keyError
#NameError
#OSError
#RuntimeError
#StopIteration
#SyntaxError
#SystemError
#TabError
#typeError
#UnboundLocalError
#valueError
#windowsError
#ZeroDivisionError
'''
