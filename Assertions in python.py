'''
পাইথনে assertion তথা স্যানিটি চেক এনাবেল বা ডিজ্যাবল করে
প্রোগ্রাম টেস্টিং এর কাজ করা হয়। কিন্তু, স্যানিটি চেক (sanity-check)
আসলে কি? খুব দ্রুত একটি স্টেটমেন্টকে পর্যবেক্ষণ করে সেটার ফলাফলের সত্যতা যাচাই
করাকেই স্যানিটি চেক বলা হয়।

assert স্টেটমেন্ট ব্যবহার করে এই কুইক টেস্ট করা হয়।

যখন পাইথন কোন প্রোগ্রামের যেকোনো যায়গায় এই assert স্টেটমেন্টটি পায় তখন
সেটাকে দ্রুত যাচাই করে এবং স্টেটমেন্টটি সত্য হোক সেটা আশা করে।
কিন্তু তা না হলে পাইথন AssertionError টাইপের এক্সেপশন থ্রো (তৈরি) করে।
'''

'''

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

'''

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))
