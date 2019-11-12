import random
import time
wordList = ['jollibee','mcdonalds','chowking', 'kfc', 'greenwich','popeyes', 'starbucks', 'goldilocks']
secretWord = random.choice(wordList)
x = len(secretWord)
lettersGuessed =[]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessWord =[]


def start():
    print ("Welcome! OwO")
    name = input("Enter your name: ")
    print ("Hello, " + name, "Let's play shall we? UwU")
    time.sleep(2)


start()

def secret():
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess has", x, "characters")
    print (' '.join(guessWord))
    time.sleep(2)
    
    print ("You can only have 3 mistakes!")
    time.sleep(2)
    print ("Typing more than 1 letter per guess will crash the game!") 
    time.sleep(2)
    print ("Tip: Fastfood restaurants, Yumyum")
    time.sleep(2)
    
def guessing():
    turns = 0

    while turns < 3:
        print ("\n", ' '.join(letters))
        guess = input("Please Choose a letter: ").lower()
        
        if guess not in letters:
            print ("That is not even a letter. . . T_T")
            turns +=1
            print("Mistakes: ", turns)
        elif guess in lettersGuessed:
            print("You already guessed that one you know. . .")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Good guess! ^_^")
                for y in range(0, x):
                    if secretWord[y] == guess:
                        guessWord[y] = guess
                        print(' '.join(guessWord))
                letters.remove(guess)
            else:
                print("I think I am in danger. . . Guess smart you know. . .")
                letters.remove(guess)
                turns += 1
                print("Mistakes: ", turns)
                if turns == 3:
                    print("D E A D")
                    print("The secret word was", secretWord)
                    break
        if '_' not in guessWord:
                        print("You guessed it right!")
                        print("I am free! Thank you!")
                        break              
secret()
guessing()

print("GAME OVER!!!")