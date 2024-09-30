# city="Ahmadabad"
# print(city)
# print(type(city))
#
# a = "Hello"
# b = "World"
# c =  a + b
# print(c) #HelloWorld
#
# a = "Hello"
# b = "World"
# c =  "Python"
# d = a + b + c
# print(d) #HelloWorldPython
#
# a = "Hello"
# b = "World"
# c = a + " "+ b
# print(c)
#
# a="Python"
# print(a*2)
# a ="Python"
# print(a*4)
#
# print("Python\t"*10)
# print("Python\n"*10)
# # /---Forward slash
# # \---Backward slash
#
# string1= "CREDENCE"
# print(string1)
# print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[3])
# print(string1[4])
# print(string1[5])
# # print(string1[6])
# # print(string1[7])
# # print(string1[8])
# # print(string1[9])


# String = 'CREDENCEAUTOMATION'
# print(String)

# print(String[0])
# print(String[3])
# print(String[17])

# print(String[0:7])
# print(String[5:10])

# print(String[0:8])

# print(String[8:0])
# print(String[-1])
# print(String[-3])
# print(String[-13:-10])
# print(String[3:-10])

# print(String[-10:-13])


# print(String[3:-16]) # NO RESULT
# print(String[3:-18]) # NO RESULT

# print(String[-3:1])
# print(String[-3:18])
# print(String[-2:-5])
# print(String[-5:-2])

# print(String[0:])
# print(String[8:])
# print(String[:1])
# print(String[:8])
# print(String[-8:])
# print(String[:-8])
# print(String[1:10])
# print(String[0:8])
# print(String[0:8:2])
#
# print(String[0:8:2])
# print(String[0:8:3])

# print(String[::1])
# print(String[::2])
# print(String[::3])

# print(String[-1:-12])
# print(String[-1:-12:1])
# print(String[-12:-1])
# print(String[-12:-1:1])

# print(String[-1:-12:1])
# print(String[-1:-12:-1])
# print(String[0:8:-1])
# print(String[8:0:-1])
# print(String[7::-1])
# print(String[7:: 1])
# print(String[-12:-1:1])
# print(String[-12:-1:2])
# print(String[-12:-1:-1])
# print(String[-12:-1:1])

# Prints string in reverse
# print(String[::-1])
# a='Yusuf'
# print(a[::-1])

# # Copy string to another variable
# abc = String[:]
# print(abc)
# abc = String[0:2]
# print(abc)
# abc = String[2:7]
# print(abc)

# abc = str(String)
# print(abc)



# String[0]= "D"
# print(String)

# text= "Credence Automation Testing"
# print(text.capitalize())
# print(text.casefold())
# # print(text.lower())
# a="ßABc"
# print(a.casefold())
# print(a.lower())
# print(a.islower())
# print(a.isupper())
# print(a.upper())

# First character in each word is
# titlecase and remaining titlecase
# s = 'credence for credence'
# print(s.title())
# print(s.capitalize())
# yusuf
# Yusuf - title
# Yusuf -capitalize
#
# yusuF akshay
#
# Yusuf Akshay - title
# Yusuf akshay - capitalize

# First character in first
# word is titlecase
# s = 'credence For Credence'
# print(s.title())

# Third word has titlecase
# characters at middle
# s = 'Credence For CREDENCE'
# print(s.title())
# # # Ignore the digit 6041, hence returns True
# s = '6041 Is MY number'
# print(s.title())

# word has titlecase
# characters at middle
# s = 'cREDENCE IT'
# print(s.title())

# s = 'Credence For Credence'
# print(len(s))
#
#
# s = 'credence For Credence'
# print(len(s))
# #
# s = 'Credence For CREDENCE'
# print(len(s))
#
# s = '6041 Is My Number'
# print(len(s))
#
#
# s = 'CREDENCE'
# print(len(s))


# First character in each word is
# uppercase and remaining lowercase
s = 'Credence For Credence'
# print(s.istitle()) #True

# First character in first
# word is lowercase
s = 'credence For Credence' #False
# print(s.istitle())

# Third word has uppercase
# characters at middle
# s = 'Credence For CREDENCE' # False
# print(s.istitle())
# Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.istitle())  #True

# word has uppercase
# characters at middle
s = 'CREDENCE'
# print(s.istitle())  # false
# print(s.isupper())  # True
# print(s.islower())  # false


## Have to Revise in tomorrows class
# String='Yusufususususududususuusud'
# # # #
# print(String.count('u'))
# print(String.count('u',1,5))
# print(String.count('u',10,20))
# print(String.count('Yusuf'))
# print(String.count('su'))
# print(String.count('du'))
# print(String.count('A'))

text= "Credence Automation Testing"
# print(text.endswith("Testing"))
# print(text.endswith("g"))
# print(text.endswith("ing"))
# print(text.endswith("sting"))
# print(text.endswith("abc"))


# print(text.find('A'))
# print(text.count('A'))
#
# print(text.find('Aut'))
# print(text.find('Autom'))
# print(text.find('Automation'))
# print(text.find('e'))
# print(text.find('E'))


# print(text.format("Yusuf Sir's","Python", "Class"))
# my_string = "{}, is a {}, candidate of {}, batch"
# print(my_string.format("Mahesh", "Placed", "ct16"))
# print(my_string.format("Akash", "Placed", "ct17"))
# print(my_string.format("Priya", "Placed", "ct16"))
# print(my_string.format("Radha", "Placed", "ct17"))
# print(my_string.format("Mahesh", "still not Placed", "ct15"))
# print(my_string.format("Mukund", "failedforplacement", "ct17"))
#
# my_class = "mention your name {} and {} for verification"
# print(my_class.format("pranay","5521"))

# my_string = "{}, is a {} {} software testing for {}"
# #
# print(my_string.format("Credence", "computer", "class", "Ending"))

# my_string = "{}, is a {} {} software testing for {}"
#
# print(my_string.format("Credence", "computer", "class"))
# # Output:
# #
# # # IndexError:
# String= "CREDENCE AUTOMATION"
# print(String.index('A'))
# print(String.find('A'))
# # print(String.index('Z'))
# # print(String.find('Z'))
# print(String.index('A',1))
# print(String.index('A',9))
# print(String.index('A',10))
# print(String.index('A',10,30))


# String1="Credence"
# print(String1.isalnum()) #-- True
# #
# String1="123ACS"
# print(String1.isalnum()) #-- True
# #
# String1 = 'Credence Automation 123 TesTiNG'
# print(String.isalnum()) #—false becz of space
# #
# String1 = 'Credence_Automation_TesTiNG'
# print(String.isalnum())  #— false becz of _
# #
# String1="Credence"
# print(String1.isalnum())
#
# String = 'Credence_Automation_TesTiNG'
# String1="Credence"
# print(String1.isalpha())
# print(String.isalpha())

# #
# s = "12345"
# print(s.isdecimal())
#
# # contains alphabets
# s = "12credence34"
# print(s.isdecimal())
#
# # contains numbers and spaces
# s = "12 34"
# print(s.isdecimal())
#
#
# s = "12345"
# print(s.isnumeric())
#
# # contains alphabets
# s = "12credence34"
# print(s.isnumeric())

# contains numbers and spaces
# s = "12 34"
# print(s.isnumeric())

# s = "12345"
# print(s.isdigit())
# #
# # # contains alphabets
# s = "12credence34"
# print(s.isdigit())
#
# # contains numbers and spaces
# s = "12 34"
# print(s.isdigit())

# s = "0123"
# print(s.isnumeric())
#
# # contains alphabets
# s = "0123"
# print(s.isdigit())
#
# # contains numbers and spaces
# s = "0123"
# print(s.isdecimal())
#
#
#
#
#
#
# s = "2²"
# print(s.isnumeric())
# # #
# # # # contains alphabets
# s = "2²"
# print(s.isdigit())
# # #
# # # # contains numbers and spaces
# s = "2²"
# print(s.isdecimal())
# # #
# #
# #
# s = "ↁ"
# print(s.isnumeric())
# #
# # # contains alphabets
# s = "ↁ"
# print(s.isdigit())
# #
# # # contains numbers and spaces
# s = "ↁ"
# print(s.isdecimal())


# string = "grrks FOR grrks"
# #
# # # replace all instances of 'r' (old) with 'e' (new)
# new_string = string.replace("r", "e" )
# print(string)
# print(new_string)
#
# print(string.replace("r", "e" ))
# print(string)

#
# string = "geeks for geeks \ngeeks for geeks"
# #
# print(string)
# #
# # # Prints the string by replacing only
# # # 3 occurrence of Geeks
# print(string.replace("geeks", "Grapes"))

# Replace only a certain number of Instances using replace() in Python
# In this example, we are replacing certain numbers of words. i.e. “ek” with “a” with count=3.
#
# string = "geeks for geeks geeks geeks geeks"
# #
# # Prints the string by replacing
# # # e by a
# print(string.replace("e", "a"))
# #
# # # Prints the string by replacing only
# # # 3 occurrence of ek by a
# print(string.replace("ek", "i", 4))

# Python program to demonstrate the use of
# swapcase() method

# string = "gEEksFORgeeks"
# #
# # # prints after swapping all cases
# print(string.swapcase())
# #
# string = "geeksforgeeks"
# print(string.swapcase())
# #
# string = "GEEKSFORGEEKS"
# print(string.swapcase())
#
# String = "Credence"
# print("$".join(String))
# print(",".join(String))
# print(" ".join(String))
# print(" and ".join(String))

#
s1 = 'abc'
s2 = '123'
s3 = "2525"
# #
# # # each element of s2 is separated by s1
# # # '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1 ko join kiya s2 ke sath:', s1.join(s2))
print('s1 ko join kiya s2 ke sath:', "abc".join(s2))
# #
# # # each element of s1 is separated by s2
# # 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2 ko join kiya s1 ke sath:', s2.join(s1))
print('s2 ko join kiya s1 ke sath:', s2.join(s1))

print('s3ko join kiya s1 ke sath:', s3.join(s1),s3.join(s2))
