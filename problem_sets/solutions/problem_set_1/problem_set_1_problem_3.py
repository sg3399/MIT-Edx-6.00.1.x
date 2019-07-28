#Problem Set 1 Problem 3
#Author:Siddhant Gokhale
        
#Problem Statement
#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters 
#occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print: 
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

#Inputing a string of lowercase characters
s = input('Please enter a string of lowercase characters:')

current_alphabetical_string= ""
#This stores the current alphabetical order in formation in the loop
#It is initialized as an empty string

current_alphabetical_string_count = 0
#This counts  the number of alphabets in the current alphabetical order 
#formation in the loop
#It is initialized to 0

max_alphabetical_string_count = 0
#This keeps track of the the count of the maximum alphabetal order formation 
#till now in the loop.
#It is initialized to 0


max_alphabetical_string = ""
#This keeps track of the maximum alphabetical order string till now in the loop
#It is initialized as an empty string

for i in range(len(s)):
    if i == 0:
    #Start the process. The current alphabetical string should 
    #start with the first letter, and the count should start with 1    
        current_alphabetical_string += s[i]
        current_alphabetical_string_count += 1
    #Case 1: The order is alphabetical
    #The code checks if the letter ahead is greater than the letter behind, 
    #that is, if the two letter substring is alphabetical. If this is true, 
    #it adds this to the current alphabetical string and updates the count
    elif s[i] >= s[i - 1]:
        current_alphabetical_string += s[i]
        current_alphabetical_string_count += 1
    #Case 2: The order is non-alphabetical
    #The code checks if the letter ahead is less than the letter behind, 
    #that is, if the two letter substring is not alphabetical. If this is true, 
    #and the current aphabetical count/string is greater than the max aphabetical 
    #count/string, then max aplahbetical count/string updates. Regardless, we 
    #now have to start counting again, since the alphabetical streak is broken.
    #So we initialize the string to the current letter, and the count to 1. 
    elif s[i] < s[i - 1]:
        if current_alphabetical_string_count > max_alphabetical_string_count:
        #this is greater than only since if there is a tie, we want the most 
        #first longest aplhabetical order substring
            max_alphabetical_string_count = current_alphabetical_string_count
            max_alphabetical_string = current_alphabetical_string
        current_alphabetical_string_count  = 1
        current_alphabetical_string = ""
        current_alphabetical_string += s[i]
    #If the most current alphatetical streak is greater than the last max 
    #alphabetical streak, then replace the max alphabetical streak
    if i == len(s) - 1:
        if  current_alphabetical_string_count > max_alphabetical_string_count:
                max_alphabetical_string_count = current_alphabetical_string_count
                max_alphabetical_string = current_alphabetical_string
print("Longest substring in alphabetical order is:", max_alphabetical_string)

