def sponge_case(sentence):
    """
    input a string 
    return a string with first word is lowercase and then following word is gonna be uppercase
    if string one letter , return loswercase
    assume string is all letters with / with out spaces
    """
    
    #intialize new_word with empty list 
    new_list = []
    is_lower = True
    for i in range(len(sentence)):
        letter = sentence[i]
        if letter == " ":
            new_list.append(letter)   
            is_lower = True
        else:
            if is_lower:
                new_list.append(letter.lower())
            else:
                new_list.append(letter.upper())
                
            is_lower = not is_lower
                
   
    new_word = "".join(new_list)
    
    return new_word
    
    

# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP") == "wHaT iS uP"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print(sponge_case("All tests passed!"))
print("Discuss time and space complexity if there's time remaining")