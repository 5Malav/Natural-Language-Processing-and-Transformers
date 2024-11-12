# -*- coding: utf-8 -*-
"""Part 1- Working with Text Files with Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S6qInKJE5ebfVjnCNRkYUF2QimlkBiR-

# Working with Text Files
"""

# Old way of printing text

person = "Maya"

print("MY Mother name is {}".format(person))

# Let's try new way.

# Formatted string literals or f-string literals for short.

print(f"My mother name is {person}")

# If we forget to add f before "text" then it will print
# literally text.

d = {"a":123,"b":456}

print(f"my number is {d['a']}")

ls = [1,2,3,4,5]

print(f"my number is {ls[0]}")

# Alignment and padding

# When we are dealing with multiple items that we are
# trying to print.

library = [
    ('Author','Topic','Pages'),
    ('Twain','Rafting',601),
    ('Feynman','Physics',95),
    ('Hamilton','Mythology',144)
]
print(library)

for book in library:
    print(book)

for book in library:
    print(f"Author is {book[0]}")

# Tuple unpacking
for Author,Topic,Pages in library:

    print(f"{Author}    {Topic}        {Pages}")

"""
From the above notice we can notice that it looks like formatting
is slightly sloppy here and that's because we essentially did
not use any sort of padding or any sort of space.

So first thing we can do is we can pass an argument for a
minimuim width.

Essentially a minimum width that each of these so called columns
could take
Syntax :- {column name:{10}} 10 is minimum width

we can also use like {column name:>{10}} if name is too long
"""

library = [
    ('Author','Topic','Pages'),
    ('Twain','Rafting in river',601),
    ('Feynman','Physics',95),
    ('Hamilton','Mythology',144)
]
for i in library:
    print(i)

print(" ")

for Author,Topic,Pages in library:

    print(f"{Author:{10}}{Topic:{19}}{Pages:>{4}}")

#>4 means that 4 spaces before pages entries

#to check  we can add '-' before number

print("")

for Author,Topic,Pages in library:

    print(f"{Author:{10}}{Topic:{19}}{Pages:->{10}}")

# Date formatting

from datetime import datetime

today = datetime(year=2024,month=11,day=11)


print(f"{today}")

print(f"{today:%B , %d , %Y}")

# Commented out IPython magic to ensure Python compatibility.
# # Create a Text file.
# 
# %%writefile maya.txt
# 
# Hello My name is Malav.
# I am Machine Learning engineer.
# 
#

# Open text file.

my_file = open("/content/maya.txt")

my_file

my_file.read()

# we can't call read() mutiple time in Python.
# Essentially what's going on is you have a cursor
# at the very beginning of a text file and after you call
# .read() that cursor goes throughout the entire text file
# and return the entire file as string as can see in output
# and the cursor is sitting at the end of the file.
# which means when you call read again it's just going to
# read from cursor all the way to the end of the file,
# which in this case since .read() already called , there is
# nothing there its just and empty string.

my_file.read()

# In order to fix this what we need to do is call my_file.seek
# and then you can change the cursor to index position zero
# which essentially resets the cursor and it will report back
# to zero position meaning cursor is now at beginning at the
# text file and .read() can be called again.

my_file.seek(0)

my_file.read()

my_file.seek(0)
data= my_file.read()
print(data) # to print data in different lines.

# Always close a file once done working with it.

my_file.close()

# The reason to close file is that in case if trying to opening
# that text file for another program if file is still open
# in Python it may cause issues with operating system.

# if we try to pull out USB drive its says
# hey some files are already in use.

# To read each line as separate item

my_file=open("/content/maya.txt")

my_file.readlines()

my_file.seek(0)

my_lines = my_file.readlines()
my_lines

# Iterate through my_lines

for line in my_lines:
    print(line)

# By default open function only allows us to read the file
# and that's really for safetly because by default we probably
# don't want to just have any user have write access to your
# text files otherwise they will be able to overwrite anything.

# Let's learn how to write to file and then appending to a file.
# w+ allows both read and write to a file.

# w+ should be used with caustion.
# If we open a file with w or w+ it performs a trucation
# on the original, that means anything in the original file
# is actually overwritten and deleted over.

my_file= open("/content/maya.text",mode="w+")

my_file.seek(0)
my_file.read()

# output is empty string.
# because by opening with w+ we are not overriding the
# original maya.txt file.
# So that's why w/w+ should be used with caution.
# only should be used when itent to completely overwrite the
# original contents of the file.

my_file.write("My father name is Mrugesh")

my_file.seek(0)
my_file.read()

my_file.close()

# w/w+ overwrite and delete completely
# but in case if we don't want to do that
# we can use an append method.
# Append method keep old information and then allow you to
# add in new lines.
# if the file does not exist append method will create new file
# as well.

my_file=open("/content/maya.txt","a+")

new_file = open("Mrugesh.txt","a+")
# created new file name mrugesh.text

new_file.write("I will get a job as AI engineer in 6 months")

new_file.seek(0)

new_file.read()

new_file.close()

my_file=open("/content/Mrugesh.txt",'a+')

my_file.write(',I will learn NLP and Computer vision')

my_file.seek(0)

my_file.read()

my_file.close()

# Conetext manager to automatically close the file.

with open("/content/Mrugesh.txt",'r') as my_new_file:
    my_new_variable =my_new_file.readlines()

# above code will automatically close file.

my_new_variable



