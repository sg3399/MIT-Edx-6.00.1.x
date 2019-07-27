#Problem Set 1 Problem 1
#Author:Siddhant Gokhale

#Problem Statement
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print: 
#Number of vowels:5

#Inputing a string of lowercase characters
s = input('Please enter a string of lowercase characters:')

#This will store the number of vowels found in s. This is intially set to zero.
#As we find a vowel. this number will update.
vowel_count=0

#For each lowercase character in s, this loop will (1) check if it is vowel, 
# and (2) if the character is indeed a vowel, it will add this to the vowel
#counter, vowel_count. As a result, at the end of the loop, vowel_counter will
#have the number of vowels in the string  

for c in s:
    if c=="a" or  c=="e" or c=="i" or c=="o" or c=="u":
        vowel_count += 1
print('Number of vowels:',vowel_count) 



