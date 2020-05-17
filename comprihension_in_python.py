#list comprihension:

my_list = [i**2 for i in range(20) if i %2 == 0]
print(my_list)

'''
    আউটপুট এক্সপ্রেশন: i**2

    ইনপুট সিকুয়েন্স: for i in range(20)

    কন্ডিশনাল লজিক (অপশনাল): if i % 2 == 0
'''

#set comprihension :

a_list = ['Maateen', 'Khan', 'Maksudur', 'a', 'b', 'c']
my_set = {i for i in a_list if len(i) > 1}
print(my_set)

#dictionary comprihension:
a_list = ['name', 'country', 'career']
b_list = ['Maateen', 'Bangladesh', 'TeleTalk']
my_dict = {i:j for i, j in zip(a_list , b_list)}
print(my_dict)

'''
#another type :
a = [i for i in range(11)]
print(a)
b = [i for i in range(11,21)]
print(b)
c = zip(a, b)
print(c) #error dibe 
print(list(c)) # without error , correct code
'''


my_dict = {'career': 'TeleTalk', 'country': 'Bangladesh', 'name': 'Maateen'}
new_dict = {key:value for value, key in my_dict.items()}
print(new_dict)






















