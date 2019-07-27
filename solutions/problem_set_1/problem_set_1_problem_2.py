#Problem Set 1 Problem 2
#Author:Siddhant Gokhale

#Problem Statement
#Assume s is a string of lower case characters.Write a program that prints the 
#number of times the string 'bob' occurs in s.
#For example,if s='azcbobobegghakl', then your program should print, 
#Number of times bob occurs is: 2

#Inputing a string of lowercase characters
s = input('Please enter a string of lowercase characters:')


#Recall if s is a string, then the expression s[start:end] denotes the substring
#of s that starts at the index, start and ends at the index, end-1. 

#To begin with we want to look at s[0:3], that is, the substring of s, that 
#contains the first three letters in s
start=0
end=3
#As we move onto subsequent substrings of three characters, this variable will
#store something if a bob occurs. Before we look for bob's, we peg this to zero.
no_of_bobs=0


#The while loop does the following. It looks at the first three characters, 
#s[0,3], and checks if it says "bob". If yes, it counts it in the variable, 
#no_of_bobs.If not, it goes to the next three characters, s[1,4], 
#and again checks if it says "bob". If yes, it adds this to the count of bobs 
#in the variable no_of_bobs. This continues till we reach the final three 
#characters of the sequence of lowercase characters, s.

while (end<=len(s)):
    if s[start:end]=='bob':
        no_of_bobs += 1
    start += 1
    end +=1
print('Number of times bob occurs is:', no_of_bobs)