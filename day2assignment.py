# -*- coding: utf-8 -*-
"""Day2Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13sNH09s5li1jTpPIARgEm24av6sWH31D
"""

#Question no1 : List and its functions

#list is Mutable Data Type (Modification is allowed); 
#List is also collection of objects sepearated by comma but enclosed within square brackets .

l1 = [1, 'a' , 3.14 , True ]

l1

l1[0] #intex at 0

l1[-1] #intex at -1

l1[1:3]

#Changing , adding or popping Element is possible in list

l2 = [ 23 , "Avenger" , 3.14 , True , "Apple" , 45]

l2

l2[0] =100 #replacing index 23 to 100

l2

l2.append(-93.72) #adding value to list

l2

l2.pop(-2) #delete the value from list

l2

#Modifying list - reversing , inserting , sorting

l2

l2.reverse() #reversing order of index in list

l2

l2.insert(1,"Tiger zinda hai") #inserting new value in list

l2

l3 = ["e","d","a","z","s","y","u","k","t"]

l3

l3.sort()

l3

#List - Basic Operation

l1

l2

l1+l2 #adding two List

l1

l1*4 #multplying list

#question 2 : Dictionary and its Values.

#Dictonary is a collection of object ( variable) as a key value pair . Each key is seperated from its value by a colon(:),
# it items are seperated by comma ,and the whole thing is enclosed within curly braces.

#dictonary is a mutables

d1 = { "Apple" : 270 , "Mango" : 560 , "Orange" :380}

type(d1) #type of dictonaries

#Extracting values and keys

#Extracting Keys

d1

d1.keys()

d1.values()

#Modifying a Dictonary

#Adding a new element

d1

d1["Starwberry"] = 300

d1

#changing existing element

d1

d1["Mango"]=100

d1

#dictonary FUnction

#adding up one dictonary into another

batsman = {"Sachin" :100 , "dravid" :40 , "Dhoni" :67}

bowler = {"Bumrah" :4 , "irfan":33 , "zaher":4}

batsman.update(bowler)

batsman

#popping element from dictonaries

batsman

batsman.pop("Dhoni")

batsman

#Question no 3 : Define Sets and its Default Values

#set() method is used to convert any of the iterable to sequence of iterable elements with dintinct elements, commonly called Set.

s1 = ("zebra" , "veer" , "cow" , 1,3,3,4,5,5,5,5,5, "arjun")

s1

set(s1)

#removing duplication and arranging in particular order

#question no 4 : Tuple and explore default function

#tuple is a collection of objects seperated by comma enclosed within parenthesis (round brackets)

#tuple is immutable data types

tup1 = (1, "a" , True , 2,77 , 6-5j)

type(tup1)

#extracting Individual Element

tup1

tup1[0]

tup1[-2]

tup1[1:3]

#modifying tuple is not possible - immutable

#Basic Operation for Tuple

#finding length of tuple

tup1

len(tup1) #syntax for finding length of tuple

#concatenating Tuple ( Adding two tuples)

tup1

tup2 = ( 2, False , 3.14 , "Lootvilla")

tup1+tup2

tup2+tup1

#Repeating tuple element

tup1*5

#repeating and concatenating

tup1*2 + tup2

#minimum Value in Tuples

tup4 = (1,3,5,6,7,8,9,2)

min(tup4)

#maximum values in Tuples

max(tup4)

#question no 5 : Explain String and explore its default values

#String is immutable data types

#sequence of characters represent within quotes is know as a string 
#python string can defined within a pair of single or double quotes. It can be also be defined within triple single or double quotes
#Python does not support character type  , they are treated as string of lenght type.

str1 = 'This is one '

str1

str2 = "This is two"

str2

str3 = ''' This is tiger
in zoo , wild tiger  '''

str3

Saner_string = "This is Jignesh Saner"

Saner_string  #Index value and finding it

Saner_string[5]

Saner_string[-1]

Saner_string[6:-3]

#lenght of Strings

len(Saner_string)

#change variable in lower case

Saner_string.lower() #syntax .lower()

#change Variable in Upper Case

Saner_string.upper() #syntax .upper()

#replacing any index or variable value

Saner_string.replace('i','y') #syntax for replace a substring

#number of occurences of substrings

Saner_string

Saner_string.count("i") #syntax for count function

#finding the index of substring

Saner_string

Saner_string.find("Saner")

#splitting a string

Str21 = "I play cricket , volleyball , hockey"

Str21

Str21.split(",")

#end of Assignment