
# Hangman
import random 
from collections import Counter 
  
#list of movies  
Movies = '''avatar aliens titanic terminator '''
  
Movies = Movies.split(' ') 
# randomly choose a secret word from our "Movies" LIST. 
word = random.choice(Movies)

if __name__ == '__main__': # proving a hint for ease.
    print('HELLO, TIME TO PLAY HANGMAN, KEEP IN MIND, YOU MIGHT BE HANGED Guess the word! HINT: the word is a movie name directed by James Cameron') 
      
    for i in word: 
         # For printing the empty spaces or blanks for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
             # try and except is used in case of backup plan
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # conditions of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correctly 
            if guess in word: 
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    letterGuessed += guess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for W in word: 
                if W in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(W, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Congratulations, You were saved!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances and has no option other than to be hanged
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('You were hanged !!!') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('sorry', ' Try again.') 
        exit()           
