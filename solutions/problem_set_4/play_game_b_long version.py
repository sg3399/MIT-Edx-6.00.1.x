    user_input='n'
    played_hand=False
    while user_input=='n' or user_input=='r':
        #Asks the user to input 'n' or 'r' or 'e'.
        user_input=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while user_input!='n' and user_input!='r' and user_input!='e':
            print("\n Invalid command.")
            user_input=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                
        
        if user_input=='e':
                 break  
        elif user_input=='r' and played_hand==False:
            while user_input=='r':
                print('You have not played a hand yet. Please play a new hand first!')
                user_input=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if user_input=='e':
                 break
        elif (user_input=='r' and played_hand==True):
            comp_user=input('Enter u to have yourself play, c to have the computer play: ')
            while comp_user!='c' and comp_user!='u':
                print("\n Invalid command.")
                comp_user=input('Enter u to have yourself play, c to have the computer play: ')
            if comp_user=='u':
                playHand(hand, wordList, HAND_SIZE) 
            else:
                compPlayHand(hand, wordList, HAND_SIZE)
        else:
            comp_user=input('Enter u to have yourself play, c to have the computer play: ')
            while comp_user!='c' and comp_user!='u':
                print("\n Invalid command.")
                comp_user=input('Enter u to have yourself play, c to have the computer play: ')
            
            hand= dealHand(HAND_SIZE)
            played_hand=True
            if comp_user=='u':
                playHand(hand, wordList, HAND_SIZE) 
            else:
                compPlayHand(hand, wordList, HAND_SIZE)