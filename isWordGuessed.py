secretWord=str(input("Enter the word to be guessed: "))
x=len(secretWord)
print("The word has", x, "letters.")
lettersGuessed=input("Enter a list of letters: ")

def isWordGuessed(secretWord, lettersGuessed):
    for a in secretWord:
        y = a in lettersGuessed
        if y == "False":
            break
        
    return y 
print (isWordGuessed(secretWord, lettersGuessed))