secretWord = str(input("Enter the word to be guessed: "))
lettersGuessed = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   
def getAvailableLetters():
    me=0
    while me == 0:
        lettersGuessed = input("Type a letter: ").lower()

        if lettersGuessed in secretWord:
            letters.remove(lettersGuessed)
        else:
            letters.remove(lettersGuessed)
                
        print ("These are the available words:\n")
        print (''.join(letters))

    return me
getAvailableLetters()