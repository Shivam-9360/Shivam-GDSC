#<--Helper functions-->
# Returns the next character
def nextCharacter(character):
    newCharacter = ""
    if(character == "z"):
        newCharacter = "a"
    elif(character == "Z"):
        newCharacter = "A"
    else:
        newCharacter = chr(ord(character)+1)
    return newCharacter

# Returns if it is a vowel or not
def isVowel(character):
    return (character == "a" or
            character == "e" or 
            character == "i" or 
            character == "o" or 
            character == "u" or 
            character == "A" or 
            character == "E" or 
            character == "I" or 
            character == "O" or 
            character == "U")
    
#<--Main Code-->
def StringManipulation(string):
    # Succeeding alphabet
    output_1 = ""
    for character in string:
        if(character.isalpha()):
            output_1 = output_1 + nextCharacter(character)
        else:
            output_1 = output_1 + character
    print(output_1)
    
    # Inverted after removing all vowels
    output_2 = ""
    for character in output_1:
        if(character.isalpha()):
            if(not isVowel(character)):
                output_2 = character + output_2
        else:
            output_2 = character + output_2
    print(output_2)
    
    # Every alternate character
    output_3 = ""
    alternate = True
    for character in string:
        if(alternate):
            output_3 = output_3 + character
        alternate = not alternate
    print(output_3)
    
    
StringManipulation("ComputerProgrammingIsForGeeks1234")

