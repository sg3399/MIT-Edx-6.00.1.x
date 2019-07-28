    print('Please think of a number between 0 and 100!')

low=0
high=100
guess=int((low+high)/2)
x='l'

while x=='l' or x=='h':
    x=input("Is your secret number"+" "+str(guess)+"?\n"+"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n\n"+"Please enter here:")
    while x!='l' and x!='h' and x!='c':
        print("\nSorry, I did not understand your input.")
        x=input("Is your secret number"+" "+str(guess)+"?\n"+"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n\n"+"Please enter here:")
    if x=='l':
        low=guess
        guess=int((low+high)/2)
    elif x=='h':
        high=guess  
        guess=int((low+high)/2)
    else:
        print("\nGame over. Your secret number was:", str(guess))

            
        


