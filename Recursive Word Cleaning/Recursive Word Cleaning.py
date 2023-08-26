def Clean_Word(word):
    
    print(f"Word Before if Condition => {word}")   
    
    # Here Check if length of word Equal to 1 , if it is true it Will Store word in Clean_Word Function
    if len(word) == 1: # Base Case 
        return word
    
    # here check if first letter equal to secound letter , if it is true it will remove first letter and it repeat the process , until fist letter not equal secound letter , so it will goto the secound if condition.
    if word[0] == word[1]: # WWWooorrrdd
        print(f"Word in the if Condition => {word}")    

        return Clean_Word(word[1:])
    print(f"Word Before return => {word}")
    
    # Here Return function => Store the fist letter from first if condition Then recursive call function to be excuted Again And repeat the process .
    return word[0] + Clean_Word(word[1:]) # Wooorrrdd
    
    # Stash [  word  ]
print(Clean_Word("WWWooorrrdd"))