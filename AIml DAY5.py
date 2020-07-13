# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:16:33 2020

@author: DELL
"""

#Question 1 : Write a Python program to find the first 20 non-even prime natural numbers.

x= range(0,20)
for seq in x:
    print(seq)
    

number = 100
for num in range(2,number + 1):
       if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                     break
            else:
                if(num%2!=0):
                    print(num)


#Question 2 : Write a Python program to implement 15 functions of string.                    
 
value = 'Welcome to Python sumit'
print(value.split())

value = 'Welcome to Python Sumit'
text = value[10:]
print(text)

msg = 'Python is easy to learn?'
a = msg.find("easy")
print(a)

msg = 'Python anaconda'
print(len(msg))

msg = "welcome to python"
print(msg.upper())

msg = "Hi Ganesh"
store = msg.startswith('Hi')
print(store)

msg = "John is good but John talk less"
store = msg.count("John")
print(store)

msg = "Hello John, how are you"
store = ('how' in msg)
print(store)

name1 = 'Python is good'
name2 = 'Python is good'
if name1 == name2:
    print(name1,'is equal to',name2)

name1 = 'Python is good'
name2 = 'Python good'
if name1 != name2:
    print(name1,'is NOT equal to',name2)

s = 'WelCome to MyPy'
print(s.capitalize())

s = 'ABCDBCA'
translation = s.maketrans('A', 'a')
print(s.translate(translation))
translation = s.maketrans('ABCD', 'abcd')
print(s.translate(translation))



#Question 3: Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
#Display the message accordingly to the user.

def isPalindrome(s): 
    return s == s[::-1] 

def isAnagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)


str1 = "lives"
str2 = "elviss"

if(isPalindrome(str1)):
    print("Palindrome")
elif(isAnagram(str1,str2)):
    print("Anagram")
else:
    print("None")


#
#Question 4: Write a Python's user defined function that removes all the additional characters from the string and converts it finally to lower case using built-in lower().
 #eg: If the string is "Dr. Darshan Ingle @AI-ML Trainer", then the output be "drdarshaningle aimltrainer".  


def formatString(org_string):
    list_of_char = ['.', '@', ' ','-']
    # Remove all occurrence of a characters 's', 'a' & 'i' from the string
    mod_string = org_string.translate( {ord(elem): None for elem in list_of_char} )
    return mod_string.lower()

org_string = "i want to be a data scientist"
# Remove all occurrence of a character '. @ spaces' from the string

print(formatString(org_string))  