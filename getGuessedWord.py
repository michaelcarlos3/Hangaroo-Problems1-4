secretWord = input("Please enter the word to be guessed: ")
x = len(secretWord)
lettersGuessed = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessWord =[]


def getGuessedWord():
    
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess has", x, "characters")
    print (' '.join(guessWord))
    
    turns = 1
    
    while turns < 3:
        
        guess = input("Enter a letter: ").lower()
        
        if guess not in alphabet:
            print ("That is not a letter!")
        elif guess in lettersGuessed:
            print("That letter has already been used!")
        elif guess not in secretWord:
            print("Try again!\n")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Good work!")
                for y in range(0, x):
                    if secretWord[y] == guess:
                        guessWord[y] = guess
                        print(' '.join(guessWord))
                        
        if '_' not in guessWord:
                        print("Congratulations!")
                        break

getGuessedWord()