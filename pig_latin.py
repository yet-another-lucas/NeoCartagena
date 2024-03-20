# a function to apply pig latin to a string
def translate(word: str) -> str:
    # if the word starts with a vowel
    if word[0] in "aeiou":
        # add way to the end of the word
        word = word + "way"
    # if the word starts with a consonant
    else:
        # move the first letter to the end of the word
        word = word[1:] + word[0]
        # add ay to the end of the word
        word = word + "ay"
    # return the pig latin word
    return word
