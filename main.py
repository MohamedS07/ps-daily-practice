# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.

def split_string(content):
    a = content.split('-')
    for i in a:
        print(i)

split_string('the-sun-rises-in-west')


def split_string(content):
    e = ""
    for j in content:
        if j != '-':
            e += j
        else:
            print(e)
            
    print(e)

split_string('the-sun-rises-in-west')
split_string('the sun rises in west')



# 2. Write a Python program to reverse a given string in two ways:
#- Using an inbuilt function or slicing
#- Without using any inbuilt functions/Slicing

def slice_string(content):
    a = content[::-1]
    print(a)

slice_string ('Python')
slice_string ('Java')


def slice_string(content):
    e = ""
    for j in content:
        e = j + e
    print(e)

slice_string ('Python')
slice_string ('Java')


# 3. Write a Python program to count the number of consonants in a given string.

def consonants_check(consonants):
    letter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for foo in consonants:
        if foo in letter:
            count += 1
    print("Number of consonants:", count)

consonants_check('hello world')
consonants_check('Welcome')


# 4.  Write a Python program to remove all spaces from a given string.

def space_remove (content):
    empty = ""
    for i in content:
        if i != " ":
            empty += i
    print(empty)

space_remove('hello world')
space_remove('Welcome to the world')

# Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:







